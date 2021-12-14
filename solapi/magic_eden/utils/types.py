from datetime import datetime
from typing import TypedDict


class CollectionStats(TypedDict):
    listed_count: int
    floor_price: float
    listed_total_value: float
    day_avg_price: float
    day_volume: float
    total_volume: float


class CollectionInfo(TypedDict):
    symbol: str
    name: str
    image_url: str
    description: str
    created: datetime
    website: str
    twitter: str
    discord: str
    has_all_items: bool
