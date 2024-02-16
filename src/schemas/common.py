from enum import StrEnum


class EnvType(StrEnum):
    PROD = "prod"
    DEV = "dev"
    TEST = "test"


class TableName(StrEnum):
    RECEIPT = "receipt"
    PURCHASE = "purchase"
    PRODUCT_BARCODE = "product_barcode"
    SHOP_OSM = "shop_osm"


class TablePartitionKey(StrEnum):
    RECEIPT = "user_id"
    PURCHASE = "shop_id"
    PRODUCT_BARCODE = "shop_id"
    SHOP_OSM = "country_code"
