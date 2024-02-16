import os

from schemas.common import EnvType, TableName, TablePartitionKey
from adapters.db.cosmos_db_core import CosmosDBCoreAdapter


def migrate_db():
    env = os.environ.get("ENV_NAME", EnvType.DEV)
    session = CosmosDBCoreAdapter(env)
    session.create_db()
    tables = {
        TableName.RECEIPT: TablePartitionKey.RECEIPT,
        TableName.PURCHASE: TablePartitionKey.PURCHASE,
        TableName.PRODUCT_BARCODE: TablePartitionKey.PRODUCT_BARCODE,
        TableName.SHOP_OSM: TablePartitionKey.SHOP_OSM,
    }
    for table, partition_key in tables.items():
        session.create_table(table, partition_key)


if __name__ == "__main__":
    migrate_db()
