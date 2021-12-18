from datetime import datetime
from typing import TypedDict


class MECollectionStats(TypedDict):
    listed_count: int
    floor_price: float
    listed_total_value: float
    day_avg_price: float
    day_volume: float
    total_volume: float


class MECollectionInfo(TypedDict):
    symbol: str
    name: str
    image_url: str
    description: str
    created: datetime
    website: str
    twitter: str
    discord: str
    has_all_items: bool
    supply: int


class MECollectionMetrics(TypedDict):
    symbol: str
    total_volume: float
    daily_volume: float
    weekly_volume: float
    monthly_volume: float
    prev_daily_volume: float
    prev_weekly_volume: float
    prev_monthly_volume: float
    avg_price: float
    daily_avg_price: float
    weekly_avg_price: float
    monthly_avg_price: float
    prev_daily_avg_price: float
    prev_weekly_avg_price: float
    prev_monthly_avg_price: float
    floor_price: float
    prev_daily_floor_price: float
    prev_weekly_floor_price: float
    prev_monthly_floor_price: float
    global_volume: float
    global_daily_volume: float
    global_weekly_volume: float
    global_monthly_volume: float
    prev_daily_global_volume: float
    prev_weekly_global_volume: float
    prev_monthly_global_volume: float
