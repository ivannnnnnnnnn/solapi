from typing import Optional, Dict, List

from solapi.magic_eden.utils.consts import MEAPIUrls
from solapi.magic_eden.utils.data import collection_stats_cleaner, collection_info_cleaner, \
    collection_list_stats_cleaner
from solapi.magic_eden.utils.types import MECollectionStats, MECollectionInfo, MECollectionMetrics
from solapi.utils.api import BaseApi


class MagicEdenCollectionApi(BaseApi):

    def get_collection_stats_dirty(self, symbol: str) -> Optional[Dict]:
        url = f'{MEAPIUrls.COLLECTION_STATS}{symbol}'
        res = self._get_request(url)
        return res.get('results') if isinstance(res, dict) else None

    def get_collection_info_dirty(self, symbol: str) -> Optional[Dict]:
        url = f'{MEAPIUrls.COLLECTION_INFO}{symbol}'
        res = self._get_request(url)
        return res if bool(res) else None

    def get_collection_stats(self, symbol: str) -> Optional[MECollectionStats]:
        data = self.get_collection_stats_dirty(symbol)
        if data:
            return collection_stats_cleaner(data)

    def get_collection_info(self, symbol: str) -> Optional[MECollectionInfo]:
        data = self.get_collection_info_dirty(symbol)
        if data:
            return collection_info_cleaner(data)

    def get_collection_list_stats_dirty(self):
        url = MEAPIUrls.COLLECTION_LIST_STATS
        res = self._get_request(url)
        return res.get('results') if isinstance(res, dict) else None

    def get_collection_list_stats(self) -> Optional[List[MECollectionMetrics]]:
        data = self.get_collection_list_stats_dirty()
        if data:
            return list(map(lambda x: collection_list_stats_cleaner(x), data))

    def get_collection_list_dirty(self):
        url = MEAPIUrls.COLLECTION_LIST
        res = self._get_request(url)
        return res.get('collections') if isinstance(res, dict) else None

    def get_collection_list(self) -> Optional[List[MECollectionInfo]]:
        data = self.get_collection_list_dirty()
        if data:
            return list(map(lambda x: collection_info_cleaner(x), data))
