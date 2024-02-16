import logging
import os
from abc import ABC
from typing import Self, Dict, Any, List

from azure.cosmos import exceptions
from azure.cosmos.cosmos_client import CosmosClient
from azure.cosmos.database import DatabaseProxy
from azure.cosmos.partition_key import PartitionKey

from src.adapters.db.base import BaseDBAdapter
from src.schemas.common import EnvType, TableName


class CosmosDBCoreAdapter(BaseDBAdapter, ABC):
    container = None
    db = None

    def __init__(self, env: EnvType):
        super().__init__(env)
        self.client = CosmosClient(
            os.environ[f"{env.upper()}_COSMOS_DB_ACCOUNT_HOST"],
            {"masterKey": os.environ[f"{env.upper()}_COSMOS_DB_ACCOUNT_KEY"]},
        )

    def use_db(self, container_id: TableName, db_id: str | None = None) -> Self:
        if not db_id:
            db_id = os.environ[f"{self.env.upper()}_COSMOS_DB_DATABASE_ID"]
        self.db = self.client.get_database_client(db_id)
        self.container = self.db.get_container_client(container_id)
        return self

    def create_one(self, data: Dict[str, Any]) -> str:
        try:
            item = self.container.create_item(data)
            return item["id"]
        except exceptions.CosmosResourceExistsError:
            return data["id"]

    def read_one(self, _id: str, **kwargs) -> Dict[str, Any]:
        partition_key = kwargs.get("partition_key")
        if partition_key is None:
            raise ValueError("partition_key is required")
        return self.container.read_item(_id, partition_key)

    def read_many(
        self,
        where: Dict[str, Any] | None = None,
        partition_key: str | None = None,
        limit=10,
        **kwargs,
    ) -> List[Dict[str, Any]]:
        if where:
            where_str, where_params = format_where(where)
            return list(
                self.container.query_items(
                    f"SELECT * FROM r WHERE {where_str}",
                    where_params,
                    partition_key,
                    max_item_count=limit,
                )
            )
        return list(self.container.read_all_items(limit))

    def update_one(self, _id: str, data: Dict[str, Any]) -> bool:
        response = self.container.replace_item(_id, data)
        return bool(response["_ts"])

    def delete_one(self, _id: str, **kwargs) -> bool:
        partition_key = kwargs.get("partition_key")
        if partition_key is None:
            raise ValueError("partition_key is required")

        self.container.delete_item(_id, partition_key)
        return True

    def create_db(self, db_id: str | None = None) -> Self:
        if not db_id:
            db_id = os.environ[f"{self.env.upper()}_COSMOS_DB_DATABASE_ID"]
        try:
            self.db: DatabaseProxy = self.client.create_database(db_id)
            logging.info("Database with id '%s' created", db_id)
        except exceptions.CosmosResourceExistsError:
            logging.info("Database with id '%s' already exists", db_id)
            self.db = self.client.get_database_client(db_id)
        return self

    def create_table(self, container_id: str, partition_key: str) -> Self:
        try:
            self.container = self.db.create_container(
                container_id, PartitionKey(path=f"/{partition_key}")
            )
            logging.info("Container with id '%s' created", container_id)
        except exceptions.CosmosResourceExistsError:
            logging.info("Container with id '%s' already exists", container_id)
            self.container = self.db.get_container_client(container_id)
        return self

    def drop_table(self, container_id: str) -> None:
        try:
            self.db.delete_container(container_id)
        except exceptions.CosmosResourceNotFoundError:
            pass

    def drop_db(self) -> None:
        try:
            self.client.delete_database(self.db)
            logging.info("Database with id '%s' dropped", self.db.id)
        except exceptions.CosmosResourceNotFoundError:
            logging.info("Database with id '%s' was not found", self.db.id)


# Function to format the where clause for CosmosDB query
def format_where(where: Dict[str, Any]) -> (str, List[Dict[str, Any]]):
    where_str = ""
    where_params = []
    for key, value in where.items():
        where_str += f"r.{key}=@{key} AND "
        where_params.append({"name": f"@{key}", "value": value})

    return where_str.rstrip(" AND "), where_params
