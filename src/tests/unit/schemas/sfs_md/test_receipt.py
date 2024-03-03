from datetime import datetime
from unittest import TestCase
from uuid import UUID

from src.schemas.common import CountryCode, CurrencyCode
from src.schemas.purchased_item import PurchasedItem
from src.schemas.sfs_md.receipt import SfsMdReceipt
from src.tests import USER_ID_1, SHOP_ID_1


class TestSfsMdReceipt(TestCase):
    def setUp(self):
        self.date = datetime.now()
        self.user_id = UUID(USER_ID_1)
        self.key = 123
        self.total_amount = 100.0
        self.purchases = [PurchasedItem(name="item", price=10.0, quantity=1)]

    def test_user_id_not_uuid(self):
        with self.assertRaises(ValueError):
            SfsMdReceipt(
                None,
                self.date,
                "NOT_UUID",
                "company_id",
                "company_name",
                CountryCode.MOLDOVA,
                "shop_address",
                "cash_register_id",
                self.key,
                CurrencyCode.MOLDOVAN_LEU,
                self.total_amount,
                self.purchases,
            )

    def test_shop_id_not_uuid(self):
        with self.assertRaises(ValueError):
            SfsMdReceipt(
                None,
                self.date,
                self.user_id,
                "company_id",
                "company_name",
                CountryCode.MOLDOVA,
                "shop_address",
                "cash_register_id",
                self.key,
                CurrencyCode.MOLDOVAN_LEU,
                self.total_amount,
                self.purchases,
                shop_id="NOT_UUID",
            )

    def test_auto_generated_fields(self):
        receipt = SfsMdReceipt(
            None,
            self.date,
            self.user_id,
            "company_id",
            "company_name",
            "country_code",  # gets replaced with 'md'
            "shop_address",
            "cash_register_id",
            self.key,
            "currency_code",  # gets replaced with 'mdl'
            self.total_amount,
            self.purchases,
            "receipt_url",
        )
        self.assertTrue(receipt.id.startswith(CountryCode.MOLDOVA))
        self.assertEqual(receipt.country_code, CountryCode.MOLDOVA)
        self.assertEqual(receipt.currency_code, CurrencyCode.MOLDOVAN_LEU)
        self.assertTrue(receipt.receipt_url.startswith("https://mev.sfs.md"))
