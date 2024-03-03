from dataclasses import dataclass
from uuid import UUID

from src.schemas.common import ItemBarcodeStatus


@dataclass
class PurchasedItem:
    name: str
    quantity: float
    price: float
    item_id: UUID | None = None
    status: ItemBarcodeStatus = ItemBarcodeStatus.PENDING
