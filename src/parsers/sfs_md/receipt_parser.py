import html
import json
import re
from datetime import datetime
from typing import Self

from src.helpers import split_list
from src.parsers.receipt_parser_base import ReceiptParserBase
from src.schemas.purchase import Purchase
from src.schemas.receipt import Receipt

RECEIPT_REGEX = r"wire:initial-data=\"(\{.*receipt\.index-component.*\})\""


class SfsMdReceiptParser(ReceiptParserBase):
    def __init__(self, user_id: int):
        super().__init__(user_id)

    def parse_html(self, page: str) -> Self:
        matches = re.search(RECEIPT_REGEX, page)
        if matches:
            self._data = json.loads(html.unescape(matches.group(1)))
        return self

    def extract_data(self) -> Receipt:
        data = split_list(
            self._data["serverMemo"]["data"]["receipt"],
            "````````````````````````````````````````````````",
        )
        date_str = data[-2][0][0][5:] + data[-2][0][1][3:]
        date = datetime.strptime(date_str, "%d.%m.%Y %H:%M:%S")

        purchases = []
        for purchase in data[1]:
            if purchase[0] != "":
                quantity, price = purchase[1].split(" x ")
                purchases.append(
                    Purchase(
                        product_name=purchase[0],
                        product_quantity=float(quantity),
                        product_price=float(price),
                    )
                )

        return Receipt(
            user_id=self.user_id,
            date=date,
            company_id=data[0][1][12:],
            company_name=data[0][0],
            country_code="MD",
            shop_address=data[0][2],
            cash_register_id=data[0][3][25:],
            receipt_id=int(data[-1][0][1]),
            total_amount=float(data[2][0][1]),
            currency_code="MDL",
            purchases=purchases,
        )
