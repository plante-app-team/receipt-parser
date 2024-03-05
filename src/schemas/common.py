from enum import StrEnum, Enum


class EnvType(StrEnum):
    PROD = "prod"
    DEV = "dev"
    TEST = "test"


class TableName(StrEnum):
    RECEIPT = "receipt"
    SHOP = "shop"
    SHOP_ITEM = "shop_item"


class TablePartitionKey(StrEnum):
    RECEIPT = "user_id"
    SHOP = "country_code"
    SHOP_ITEM = "shop_id"


class CountryCode(StrEnum):
    MOLDOVA = "md"


# https://www.six-group.com/dam/download/financial-information/data-center/iso-currrency/lists/list-one.xml
class CurrencyCode(StrEnum):
    MOLDOVAN_LEU = "mdl"


class OsmType(StrEnum):
    NODE = "node"
    WAY = "way"
    RELATION = "relation"


class ReceiptProvider(StrEnum):
    SFS_MD = "sfs_md"


class ItemBarcodeStatus(StrEnum):
    PENDING = "pending"  # barcode is not yet added
    MISSING = "missing"  # item does not have international barcode
    IRRELEVANT = "irrelevant"  # item is not relevant for the app users (e.g. car tyres)
    ADDED = "added"  # barcode is added by the user


class Operator(Enum):
    EQ = "eq"
    NE = "ne"
