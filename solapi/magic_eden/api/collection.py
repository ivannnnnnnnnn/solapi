from typing import Optional, Dict

from solapi.magic_eden.utils.consts import MEAPIUrls
from solapi.magic_eden.utils.data import collection_stats_cleaner, collection_info_cleaner
from solapi.magic_eden.utils.types import CollectionStats, CollectionInfo
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

    def get_collection_stats(self, symbol: str) -> Optional[CollectionStats]:
        data = self.get_collection_stats_dirty(symbol)
        print(data)
        if data:
            return collection_stats_cleaner(data)

    def get_collection_info(self, symbol: str) -> Optional[CollectionInfo]:
        data = self.get_collection_info_dirty(symbol)
        if data:
            return collection_info_cleaner(data)
