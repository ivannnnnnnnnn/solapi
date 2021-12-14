class MEAPIUrls:
    COLLECTION_STATS = 'https://api-mainnet.magiceden.io/rpc/getCollectionEscrowStats/'
    COLLECTION_INFO = 'https://api-mainnet.magiceden.io/collections/'


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
