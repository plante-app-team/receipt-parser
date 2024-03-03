from unittest import TestCase
from uuid import UUID

from src.schemas.common import ItemBarcodeStatus
from src.schemas.shop_item import ShopItem
from src.tests import BARCODE_1, SHOP_ID_1


class TestShopItem(TestCase):
    def setUp(self):
        self.name = "Test Item"
        self.status = ItemBarcodeStatus.ADDED

    def test_init_shop_item(self):
        item = ShopItem(None, UUID(SHOP_ID_1), self.name, self.status, BARCODE_1)
        self.assertIsInstance(item, ShopItem)

    def test_shop_id_not_uuid(self):
        with self.assertRaises(ValueError):
            ShopItem(None, "NOT_UUID", self.name, self.status, BARCODE_1)

    def test_status_not_valid(self):
        with self.assertRaises(ValueError):
            ShopItem(None, SHOP_ID_1, self.name, "INVALID_STATUS", BARCODE_1)

    def test_barcode_not_provided(self):
        with self.assertRaises(ValueError):
            ShopItem(None, SHOP_ID_1, self.name, self.status, None)

    def test_barcode_not_digit(self):
        with self.assertRaises(ValueError):
            ShopItem(None, SHOP_ID_1, self.name, self.status, "not_digit")

    def test_barcode_not_valid(self):
        with self.assertRaises(ValueError):
            ShopItem(None, SHOP_ID_1, self.name, self.status, "1111111111")

    def test_id_not_uuid(self):
        with self.assertRaises(ValueError):
            ShopItem("not_uuid", SHOP_ID_1, self.name, self.status, BARCODE_1)

    def test_id_auto_generated(self):
        item = ShopItem(None, UUID(SHOP_ID_1), self.name, self.status, BARCODE_1)
        self.assertIsInstance(item.id, UUID)
