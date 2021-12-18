class SAAPIUrls:
    COLLECTION_LIST = 'https://qzlsklfacc.medianetwork.cloud/get_collections'
    COLLECTION_STATS_LIST = 'https://qzlsklfacc.medianetwork.cloud/query_volume_all'


class SAResponseConstsCollectionInfo:
    # collection info
    ID = 'id'
    SYMBOL = 'url'
    NAME = 'name'
    DESCRIPTION = 'description'
    DISPLAY = 'display'
    NEW = 'new'
    SOON = 'soon'
    TRENDING = 'trending'
    DATE = 'date'
    SUPPLY = 'supply'
    TWITTER = 'twitter'
    WEBSITE = 'website'
    DISCORD = 'discord'
    IMG = 'imgpreview'


class SAResponseConstsCollectionStats:
    # collection stats
    TOTAL_VOLUME = 'totalVolume'
    DAILY_VOLUME = 'dailyVolume'
    WEEKLY_VOLUME = 'weeklyVolume'
    TOTAL_SALES = 'totalSales'
    DAILY_SALES = 'dailySales'
    WEEKLY_SALES = 'weeklySales'
    PREV_DAILY_SALES = 'prevDailySales'
    PREV_DAILY_VOLUME = 'prevDailyVolume'
    PREV_WEEKLY_SALES = 'prevWeeklySales'
    PREV_WEEKLY_VOLUME = 'prevWeeklyVolume'
    FLOOR_PRICE = 'floorPrice'
    OWNER_COUNT = 'ownerCount'
    SYMBOL = 'collection'
    LAST_UPDATE = 'lastUpdated'
    CATEGORY = 'category'
