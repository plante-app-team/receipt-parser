from dataclasses import dataclass


@dataclass
class Purchase:
    product_name: str
    product_quantity: float
    product_price: float
