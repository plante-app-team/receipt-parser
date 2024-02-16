from unittest import TestCase

from adapters.db.cosmos_db_core import CosmosDBCoreAdapter
from schemas.common import EnvType, TableName, TablePartitionKey
from tests.stubs.receipts.sfs_md.expected_objects import KAUFLAND_RECEIPT, LINELLA_RECEIPT


class TestCosmosDBCoreAdapter(TestCase):
    session = None

    @classmethod
    def setUpClass(cls):
        cls.session = CosmosDBCoreAdapter(EnvType.TEST)
        cls.session.create_db()

    def setUp(self):
        self.session.create_table(TableName.RECEIPT, TablePartitionKey.RECEIPT)

    def test_create_one(self):
        created_receipt_id = self.session.create_one(KAUFLAND_RECEIPT.to_dict())
        assert created_receipt_id == KAUFLAND_RECEIPT.id

    def test_read_one(self):
        created_receipt_id = self.session.create_one(KAUFLAND_RECEIPT.to_dict())
        receipt: dict = self.session.read_one(
            created_receipt_id, partition_key=KAUFLAND_RECEIPT.user_id
        )
        assert receipt["date"] == KAUFLAND_RECEIPT.date.isoformat()
        assert receipt["user_id"] == KAUFLAND_RECEIPT.user_id
        assert receipt["company_id"] == KAUFLAND_RECEIPT.company_id
        assert receipt["company_name"] == KAUFLAND_RECEIPT.company_name
        assert receipt["country_code"] == KAUFLAND_RECEIPT.country_code
        assert receipt["shop_address"] == KAUFLAND_RECEIPT.shop_address
        assert receipt["cash_register_id"] == KAUFLAND_RECEIPT.cash_register_id
        assert receipt["receipt_id"] == KAUFLAND_RECEIPT.receipt_id
        assert receipt["total_amount"] == KAUFLAND_RECEIPT.total_amount
        assert receipt["currency_code"] == KAUFLAND_RECEIPT.currency_code
        assert receipt["receipt_url"] == KAUFLAND_RECEIPT.receipt_url
        assert len(receipt["purchases"]) == len(KAUFLAND_RECEIPT.purchases)

    def test_read_all(self):
        created_receipt_id_1 = self.session.create_one(KAUFLAND_RECEIPT.to_dict())
        created_receipt_id_2 = self.session.create_one(LINELLA_RECEIPT.to_dict())
        receipts = self.session.read_many()
        assert len(receipts) == 2
        assert receipts[0]["id"] == created_receipt_id_1 == KAUFLAND_RECEIPT.id
        assert receipts[1]["id"] == created_receipt_id_2 == LINELLA_RECEIPT.id

    def test_read_many_where(self):
        self.session.create_one(KAUFLAND_RECEIPT.to_dict())
        created_receipt_id_2 = self.session.create_one(LINELLA_RECEIPT.to_dict())
        receipts = self.session.read_many(
            {"company_id": LINELLA_RECEIPT.company_id}, LINELLA_RECEIPT.user_id
        )
        assert len(receipts) == 1
        assert receipts[0]["id"] == created_receipt_id_2 == LINELLA_RECEIPT.id

    def test_update_one(self):
        total_amount = KAUFLAND_RECEIPT.total_amount
        receipt = KAUFLAND_RECEIPT.to_dict()
        self.session.create_one(receipt)
        receipt["total_amount"] = total_amount + 100
        self.session.update_one(KAUFLAND_RECEIPT.id, receipt)
        receipt = self.session.read_one(
            KAUFLAND_RECEIPT.id, partition_key=KAUFLAND_RECEIPT.user_id
        )
        assert receipt["total_amount"] == total_amount + 100

    def test_delete_one(self):
        created_receipt_id_1 = self.session.create_one(KAUFLAND_RECEIPT.to_dict())
        created_receipt_id_2 = self.session.create_one(LINELLA_RECEIPT.to_dict())
        receipts = self.session.read_many()
        assert len(receipts) == 2
        self.session.delete_one(
            created_receipt_id_1, partition_key=KAUFLAND_RECEIPT.user_id
        )
        receipts = self.session.read_many()
        assert len(receipts) == 1
        assert receipts[0]["id"] == created_receipt_id_2 == LINELLA_RECEIPT.id

    def tearDown(self):
        self.session.drop_table(TableName.RECEIPT)

    @classmethod
    def tearDownClass(cls):
        cls.session.drop_db()
