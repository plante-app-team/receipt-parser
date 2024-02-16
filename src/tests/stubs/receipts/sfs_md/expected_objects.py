from datetime import datetime

from schemas.purchase import Purchase
from schemas.receipt import Receipt

KAUFLAND_RECEIPT = Receipt(
    date=datetime(2024, 1, 17, 14, 58, 22),
    user_id=1,
    company_id="1010600022460",
    company_name="MOLDRETAIL GROUP S.R.L.",
    country_code="MD",
    shop_address="mun. Chisinau bd. Banulescu Bodoni, 57",
    cash_register_id="J403001576",
    receipt_id=135932,
    total_amount=118.04,
    currency_code="MDL",
    purchases=[
        Purchase(
            product_name="ANGROMIX-77 Lapte din soia 1l",
            product_quantity=1.0,
            product_price=14.13,
        ),
        Purchase(
            product_name="ANGROMIX-77 Lapte din soia 1l",
            product_quantity=1.0,
            product_price=14.13,
        ),
        Purchase(
            product_name="Guacamole Mediterraneo, 200 g, buc",
            product_quantity=2.0,
            product_price=19.95,
        ),
        Purchase(
            product_name="Guacamole Carribe, 200 g, buc",
            product_quantity=1.0,
            product_price=19.95,
        ),
        Purchase(
            product_name="MEGGLE Crema din branza Mascarpone " "250g",
            product_quantity=1.0,
            product_price=29.93,
        ),
    ],
)

LINELLA_RECEIPT = Receipt(
    date=datetime(2023, 10, 17, 19, 54, 18),
    user_id=1,
    company_id="1016600004811",
    company_name="KAUFLAND S.R.L.",
    country_code="MD",
    shop_address="mun Chisinau str Kiev 7",
    cash_register_id="J702003194",
    receipt_id=25312,
    total_amount=370.85,
    currency_code="MDL",
    purchases=[
        Purchase(
            product_name="VDR SALAM BISC.250G",
            product_quantity=1.0,
            product_price=16.54,
        ),
        Purchase(
            product_name="PAINE WELTMEISTE750G",
            product_quantity=1.0,
            product_price=28.95,
        ),
        Purchase(
            product_name="GUT.VARZA.MURAT.400G",
            product_quantity=1.0,
            product_price=16.9,
        ),
        Purchase(
            product_name="K-VEGGIE IAURT VANIL",
            product_quantity=1.0,
            product_price=35.0,
        ),
        Purchase(
            product_name="K-VEGGIE IAURT SOIA",
            product_quantity=6.0,
            product_price=35.0,
        ),
        Purchase(product_name="BANANE", product_quantity=1.322, product_price=28.3),
        Purchase(
            product_name="STRUGURI ALBI",
            product_quantity=2.444,
            product_price=27.7,
        ),
        Purchase(
            product_name="PERE SMARIA BUTEIR",
            product_quantity=0.288,
            product_price=39.9,
        ),
        Purchase(product_name="VINETE", product_quantity=0.672, product_price=12.3),
        Purchase(
            product_name="DOVLECEI",
            product_quantity=0.704,
            product_price=14.9,
        ),
    ],
)
