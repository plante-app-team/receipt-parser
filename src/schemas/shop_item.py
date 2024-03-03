from dataclasses import dataclass
from uuid import UUID, uuid4

from src.helpers.common import validate_barcode
from src.schemas.common import ItemBarcodeStatus
from src.schemas.schema_base import SchemaBase


# there could be more than one item with the same name in the same shop,
# it has be decided how to handle this conflict
@dataclass
class ShopItem(SchemaBase):
    id: UUID | None
    shop_id: UUID
    name: str
    status: ItemBarcodeStatus
    barcode: str | None = None

    def __post_init__(self):
        if not isinstance(self.shop_id, UUID):
            raise ValueError("Shop ID must be a UUID")

        if self.status == ItemBarcodeStatus.ADDED:
            if not self.barcode:
                raise ValueError("Barcode must be provided for added items")
            if not self.barcode.isdigit():
                raise ValueError("Barcode must be a string of digits")
            if not validate_barcode(self.barcode):
                raise ValueError("Invalid barcode")

        if self.id:
            if not isinstance(self.id, UUID):
                raise ValueError("ID must be a UUID")
        else:
            self.id = uuid4()
