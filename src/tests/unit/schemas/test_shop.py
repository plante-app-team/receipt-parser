from unittest import TestCase
from uuid import UUID

from src.schemas.common import CountryCode, OsmType
from src.schemas.osm_object import OsmObject
from src.schemas.shop import Shop


class TestShop(TestCase):
    def setUp(self):
        self.country_code = CountryCode.MOLDOVA
        self.company_id = "company_id"
        self.shop_address = "shop_address"
        self.osm_object = OsmObject(
            OsmType.NODE, 123, "7.0", "28.0", "display_name", {"street": "Sezame Street"}
        )

    def test_init_shop(self):
        shop = Shop(
            None, self.country_code, self.company_id, self.shop_address, self.osm_object
        )
        self.assertIsInstance(shop, Shop)

    def test_id_not_uuid(self):
        with self.assertRaises(ValueError):
            Shop(
                "not_uuid",
                self.country_code,
                self.company_id,
                self.shop_address,
                self.osm_object,
            )

    def test_id_auto_generated(self):
        shop = Shop(
            None, self.country_code, self.company_id, self.shop_address, self.osm_object
        )
        self.assertIsInstance(shop.id, UUID)
