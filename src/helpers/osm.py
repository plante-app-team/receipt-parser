import re

import requests

OSM_HOST = "https://www.openstreetmap.org"


def get_osm_id(osm_type: str, osm_id: str) -> str:
    return f"{osm_type[0].upper()}{osm_id}"


def lookup_osm_object(osm_type: str, osm_id: str) -> dict:
    url = (
        f"https://nominatim.openstreetmap.org/lookup"
        f"?osm_ids={get_osm_id(osm_type, osm_id)}&format=json&extratags=1"
    )
    resp = requests.get(url, timeout=5).json()
    return resp[0] if resp else {}


def validate_osm_url(url: str) -> bool:
    return url.startswith(OSM_HOST)


def parse_osm_url(url: str) -> (str, str):
    pattern = r"https://www.openstreetmap.org/(.*?)/(\d+)"
    match = re.search(pattern, url)
    if match:
        return match.groups()

    raise ValueError("Invalid OSM URL")
