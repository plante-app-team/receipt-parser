from dataclasses import dataclass

from src.helpers.osm import get_osm_id
from src.schemas.common import OsmType


@dataclass
class OsmObject:
    type: OsmType
    key: int  # unique only within each type
    lat: str
    lon: str
    display_name: str | None
    address: dict | None

    @property
    def id(self):
        return get_osm_id(self.type, str(self.key))
