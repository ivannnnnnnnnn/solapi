from solapi.solanart.utils.consts import SAResponseConstsCollectionInfo, SAResponseConstsCollectionStats
from solapi.solanart.utils.types import SACollectionInfo, SACollectionStats
from solapi.utils.data import parse_str_status
from solapi.utils.datetime import parse_timestamp


def collection_list_cleaner(item: dict) -> SACollectionInfo:
    return {
        'id': item.get(SAResponseConstsCollectionInfo.ID),
        'symbol': item.get(SAResponseConstsCollectionInfo.SYMBOL),
        'name': item.get(SAResponseConstsCollectionInfo.NAME),
        'description': item.get(SAResponseConstsCollectionInfo.DESCRIPTION),
        'display': parse_str_status(item.get(SAResponseConstsCollectionInfo.DISPLAY)),
        'new': parse_str_status(item.get(SAResponseConstsCollectionInfo.NEW)),
        'soon': parse_str_status(item.get(SAResponseConstsCollectionInfo.SOON)),
        'trending': parse_str_status(item.get(SAResponseConstsCollectionInfo.TRENDING)),
        'date': parse_timestamp(item.get(SAResponseConstsCollectionInfo.DATE)),
        'supply': item.get(SAResponseConstsCollectionInfo.SUPPLY),
        'twitter': item.get(SAResponseConstsCollectionInfo.TWITTER),
        'website': item.get(SAResponseConstsCollectionInfo.WEBSITE),
        'discord': item.get(SAResponseConstsCollectionInfo.DISCORD),
        'img': item.get(SAResponseConstsCollectionInfo.IMG),
    }


def collection_list_stats_cleaner(item: dict) -> SACollectionStats:
    return {
        'total_volume': item.get(SAResponseConstsCollectionStats.TOTAL_VOLUME),
        'daily_volume': item.get(SAResponseConstsCollectionStats.DAILY_VOLUME),
        'weekly_volume': item.get(SAResponseConstsCollectionStats.WEEKLY_VOLUME),
        'total_sales': item.get(SAResponseConstsCollectionStats.TOTAL_SALES),
        'daily_sales': item.get(SAResponseConstsCollectionStats.DAILY_SALES),
        'weekly_sales': item.get(SAResponseConstsCollectionStats.WEEKLY_SALES),
        'prev_daily_sales': item.get(SAResponseConstsCollectionStats.PREV_DAILY_SALES),
        'prev_daily_volume': item.get(SAResponseConstsCollectionStats.PREV_DAILY_VOLUME),
        'prev_weekly_sales': item.get(SAResponseConstsCollectionStats.PREV_WEEKLY_SALES),
        'prev_weekly_volume': item.get(SAResponseConstsCollectionStats.PREV_WEEKLY_VOLUME),
        'floor_price': item.get(SAResponseConstsCollectionStats.FLOOR_PRICE),
        'owner_count': item.get(SAResponseConstsCollectionStats.OWNER_COUNT),
        'symbol': item.get(SAResponseConstsCollectionStats.SYMBOL),
        'last_update': parse_timestamp(item.get(SAResponseConstsCollectionStats.LAST_UPDATE)),
        'category': item.get(SAResponseConstsCollectionStats.CATEGORY)
    }
