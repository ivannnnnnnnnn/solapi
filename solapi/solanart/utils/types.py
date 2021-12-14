from datetime import date


class SACollectionInfo:
    id: int
    symbol: str
    name: str
    description: str
    display: bool
    new: bool
    soon: bool
    trending: bool
    date: date
    supply: int
    twitter: str
    website: str
    img: str
    discord: str


class SACollectionStats:
    total_volume: float
    daily_volume: float
    weekly_volume: float
    total_sales: int
    daily_sales: int
    weekly_sales: int
    prev_daily_sales: int
    prev_daily_volume: float
    prev_weekly_sales: float
    prev_weekly_volume: float
    floor_price: float
    owner_count: int
    symbol: str
    last_update: date
    category: str
