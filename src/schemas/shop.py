from dataclasses import dataclass
from uuid import UUID, uuid4

from src.schemas.common import CountryCode
from src.schemas.osm_object import OsmObject
from src.schemas.schema_base import SchemaBase


@dataclass
class Shop(SchemaBase):
    id: UUID | None
    country_code: CountryCode
    company_id: str
    shop_address: str
    osm_object: OsmObject

    def __post_init__(self):
        if self.id:
            if not isinstance(self.id, UUID):
                raise ValueError("ID must be a UUID")
        else:
            self.id = uuid4()
