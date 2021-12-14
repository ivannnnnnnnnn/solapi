from solapi.magic_eden.utils.consts import MEResponseConstsCollectionStats, MEResponseConstsCollectionInfo
from solapi.magic_eden.utils.types import CollectionInfo
from solapi.utils.converters import convert_sol_absolute
from solapi.utils.datetime import parse_date


def collection_stats_cleaner(item: dict) -> CollectionInfo:
    return {
        'listed_count': item.get(MEResponseConstsCollectionStats.LISTED_COUNT),
        'floor_price': convert_sol_absolute(item.get(MEResponseConstsCollectionStats.FLOOR_PRICE)),
        'listed_total_value': convert_sol_absolute(item.get(MEResponseConstsCollectionStats.LISTED_TOTAL_VALUE)),
        'day_avg_price': convert_sol_absolute(item.get(MEResponseConstsCollectionStats.DAY_AVG_PRICE)),
        'day_volume': convert_sol_absolute(item.get(MEResponseConstsCollectionStats.DAY_VOLUME)),
        'total_volume': convert_sol_absolute(item.get(MEResponseConstsCollectionStats.TOTAL_VOLUME)),
    }


def collection_info_cleaner(item: dict):
    return {
        'symbol': item.get(MEResponseConstsCollectionInfo.SYMBOL),
        'name': item.get(MEResponseConstsCollectionInfo.NAME),
        'image_url': item.get(MEResponseConstsCollectionInfo.IMAGE),
        'description': item.get(MEResponseConstsCollectionInfo.DESCRIPTION),
        'created': parse_date(item.get(MEResponseConstsCollectionInfo.CREATED)),
        'website': item.get(MEResponseConstsCollectionInfo.WEBSITE),
        'twitter': item.get(MEResponseConstsCollectionInfo.TWITTER),
        'discord': item.get(MEResponseConstsCollectionInfo.DISCORD),
        'has_all_items': item.get(MEResponseConstsCollectionInfo.HAS_ALL_ITEMS)
    }
