from solapi.magic_eden.utils.consts import MEResponseConstsCollectionStats, MEResponseConstsCollectionInfo, \
    MeResponseConstsCollectionListStats as metrics
from solapi.magic_eden.utils.types import MECollectionInfo, MECollectionMetrics, MECollectionStats
from solapi.utils.converters import convert_sol_absolute
from solapi.utils.data import dict_get_recursive_safe
from solapi.utils.datetime import parse_date


def collection_stats_cleaner(item: dict) -> MECollectionStats:
    return {
        'listed_count': item.get(MEResponseConstsCollectionStats.LISTED_COUNT),
        'floor_price': convert_sol_absolute(item.get(MEResponseConstsCollectionStats.FLOOR_PRICE)),
        'listed_total_value': convert_sol_absolute(item.get(MEResponseConstsCollectionStats.LISTED_TOTAL_VALUE)),
        'day_avg_price': convert_sol_absolute(item.get(MEResponseConstsCollectionStats.DAY_AVG_PRICE)),
        'day_volume': convert_sol_absolute(item.get(MEResponseConstsCollectionStats.DAY_VOLUME)),
        'total_volume': convert_sol_absolute(item.get(MEResponseConstsCollectionStats.TOTAL_VOLUME)),
    }


def collection_info_cleaner(item: dict) -> MECollectionInfo:
    return {
        'symbol': item.get(MEResponseConstsCollectionInfo.SYMBOL),
        'name': item.get(MEResponseConstsCollectionInfo.NAME),
        'img': item.get(MEResponseConstsCollectionInfo.IMAGE),
        'description': item.get(MEResponseConstsCollectionInfo.DESCRIPTION),
        'created': parse_date(item.get(MEResponseConstsCollectionInfo.CREATED)),
        'website': item.get(MEResponseConstsCollectionInfo.WEBSITE),
        'twitter': item.get(MEResponseConstsCollectionInfo.TWITTER),
        'discord': item.get(MEResponseConstsCollectionInfo.DISCORD),
        'has_all_items': item.get(MEResponseConstsCollectionInfo.HAS_ALL_ITEMS),
        'supply': item.get(MEResponseConstsCollectionInfo.SUPPLY),
    }


def collection_list_stats_cleaner(item: dict) -> MECollectionMetrics:
    return {
        'symbol': dict_get_recursive_safe(item, metrics.SYMBOL),
        'total_volume': dict_get_recursive_safe(item, metrics.TOTAL_VOLUME),
        'daily_volume': dict_get_recursive_safe(item, metrics.DAILY_VOLUME),
        'weekly_volume': dict_get_recursive_safe(item, metrics.WEEKLY_VOLUME),
        'monthly_volume': dict_get_recursive_safe(item, metrics.MONTHLY_VOLUME),
        'prev_daily_volume': dict_get_recursive_safe(item, metrics.PREV_DAILY_VOLUME),
        'prev_weekly_volume': dict_get_recursive_safe(item, metrics.PREV_WEEKLY_VOLUME),
        'prev_monthly_volume': dict_get_recursive_safe(item, metrics.PREV_MONTHLY_VOLUME),
        'avg_price': dict_get_recursive_safe(item, metrics.AVG_PRICE),
        'daily_avg_price': dict_get_recursive_safe(item, metrics.DAILY_AVG_PRICE),
        'weekly_avg_price': dict_get_recursive_safe(item, metrics.WEEKLY_AVG_PRICE),
        'monthly_avg_price': dict_get_recursive_safe(item, metrics.MONTHLY_AVG_PRICE),
        'prev_daily_avg_price': dict_get_recursive_safe(item, metrics.PREV_DAILY_AVG_PRICE),
        'prev_weekly_avg_price': dict_get_recursive_safe(item, metrics.PREV_WEEKLY_AVG_PRICE),
        'prev_monthly_avg_price': dict_get_recursive_safe(item, metrics.PREV_MONTHLY_AVG_PRICE),
        'floor_price': dict_get_recursive_safe(item, metrics.FLOOR_PRICE),
        'prev_daily_floor_price': dict_get_recursive_safe(item, metrics.PREV_DAILY_FLOOR_PRICE),
        'prev_weekly_floor_price': dict_get_recursive_safe(item, metrics.PREV_WEEKLY_FLOOR_PRICE),
        'prev_monthly_floor_price': dict_get_recursive_safe(item, metrics.PREV_MONTHLY_FLOOR_PRICE),
        'global_volume': dict_get_recursive_safe(item, metrics.GLOBAL_VOLUME),
        'global_daily_volume': dict_get_recursive_safe(item, metrics.GLOBAL_DAILY_VOLUME),
        'global_weekly_volume': dict_get_recursive_safe(item, metrics.GLOBAL_WEEKLY_VOLUME),
        'global_monthly_volume': dict_get_recursive_safe(item, metrics.GLOBAL_MONTHLY_VOLUME),
        'prev_daily_global_volume': dict_get_recursive_safe(item, metrics.PREV_DAILY_GLOBAL_VOLUME),
        'prev_weekly_global_volume': dict_get_recursive_safe(item, metrics.PREV_WEEKLY_GLOBAL_VOLUME),
        'prev_monthly_global_volume': dict_get_recursive_safe(item, metrics.PREV_MONTHLY_GLOBAL_VOLUME)
    }
