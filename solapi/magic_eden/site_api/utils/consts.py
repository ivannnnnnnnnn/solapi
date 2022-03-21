class MEAPIUrls:
    COLLECTION_STATS = 'https://api-mainnet.magiceden.io/rpc/getCollectionEscrowStats/'
    COLLECTION_INFO = 'https://api-mainnet.magiceden.io/collections/'
    COLLECTION_LIST = 'https://api-mainnet.magiceden.io/all_collections'
    COLLECTION_LIST_STATS = 'https://api-mainnet.magiceden.io/rpc/getAggregatedCollectionMetrics'


class MEResponseConstsCollectionStats:
    # STATS
    LISTED_COUNT = 'listedCount'
    FLOOR_PRICE = 'floorPrice'
    LISTED_TOTAL_VALUE = 'listedTotalValue'
    DAY_AVG_PRICE = 'avgPrice24hr'
    DAY_VOLUME = 'volume24hr'
    TOTAL_VOLUME = 'volumeAll'


class MEResponseConstsCollectionInfo:
    # INFO
    SYMBOL = 'symbol'
    NAME = 'name'
    IMAGE = 'image'
    DESCRIPTION = 'description'
    CREATED = 'createdAt'
    WEBSITE = 'website'
    TWITTER = 'twitter'
    DISCORD = 'discord'
    HAS_ALL_ITEMS = 'hasAllItems'
    SUPPLY = 'totalItems'


class MeResponseConstsCollectionListStats:
    SYMBOL = 'symbol'
    TOTAL_VOLUME = 'txVolumeME.valueAT'
    DAILY_VOLUME = 'txVolumeME.value1d'
    WEEKLY_VOLUME = 'txVolumeME.value1d'
    MONTHLY_VOLUME = 'txVolumeME.value30d'
    PREV_DAILY_VOLUME = 'txVolumeME.prev1d'
    PREV_WEEKLY_VOLUME = 'txVolumeME.prev3d'
    PREV_MONTHLY_VOLUME = 'txVolumeME.prev30d'
    AVG_PRICE = 'avgPrice.valueAT'
    DAILY_AVG_PRICE = 'avgPrice.value1d'
    WEEKLY_AVG_PRICE = 'avgPrice.value7d'
    MONTHLY_AVG_PRICE = 'avgPrice.value30d'
    PREV_DAILY_AVG_PRICE = 'avgPrice.prev1d'
    PREV_WEEKLY_AVG_PRICE = 'avgPrice.prev7d'
    PREV_MONTHLY_AVG_PRICE = 'avgPrice.prev30d'
    FLOOR_PRICE = 'floorPrice.valueAT'
    PREV_DAILY_FLOOR_PRICE = 'floorPrice.prev1d'
    PREV_WEEKLY_FLOOR_PRICE = 'floorPrice.prev7d'
    PREV_MONTHLY_FLOOR_PRICE = 'floorPrice.prev30d'
    GLOBAL_VOLUME = 'txVolume.valueAT'
    GLOBAL_DAILY_VOLUME = 'txVolume.value1d'
    GLOBAL_WEEKLY_VOLUME = 'txVolume.value7d'
    GLOBAL_MONTHLY_VOLUME = 'txVolume.value30d'
    PREV_DAILY_GLOBAL_VOLUME = 'txVolume.prev1d'
    PREV_WEEKLY_GLOBAL_VOLUME = 'txVolume.prev7d'
    PREV_MONTHLY_GLOBAL_VOLUME = 'txVolume.prev30d'
