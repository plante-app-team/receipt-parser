import os

from src.schemas.common import EnvType, TableName, TablePartitionKey
from src.adapters.db.cosmos_db_core import CosmosDBCoreAdapter


def migrate_db():
    env = os.environ.get("ENV_NAME", EnvType.DEV)
    session = CosmosDBCoreAdapter(env, logger)
    session.create_db()
    tables = {
        TableName.RECEIPT: TablePartitionKey.RECEIPT,
        TableName.PRODUCT: TablePartitionKey.PRODUCT,
        TableName.SHOP: TablePartitionKey.SHOP,
        TableName.SHOP_ITEM: TablePartitionKey.SHOP_ITEM,
    }
    for table, partition_key in tables.items():
        session.create_table(table, partition_key=partition_key)


if __name__ == "__main__":
    migrate_db()
