from datetime import datetime


def parse_date(date: str):
    try:
        return datetime.fromisoformat(date.replace('T', ' ').replace('Z', '').split('.')[0])
    except (ValueError, TypeError, AttributeError):
        return None


def parse_timestamp(ts: int):
    try:
        return datetime.fromtimestamp(ts)
    except (ValueError, TypeError):
        return None
