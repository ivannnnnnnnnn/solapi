from typing import Optional, List, Dict

from solapi.solanart.utils.consts import SAAPIUrls
from solapi.solanart.utils.data import collection_list_cleaner, collection_list_stats_cleaner
from solapi.solanart.utils.types import SACollectionInfo, SACollectionStats
from solapi.utils.api import BaseApi


class SolanartCollectionApi(BaseApi):

    def get_collection_list_dirty(self) -> Optional[List[Dict]]:
        url = SAAPIUrls.COLLECTION_LIST
        return self._get_request(url)

    def get_collection_list(self) -> Optional[List[SACollectionInfo]]:
        data = self.get_collection_list_dirty()
        if data:
            return list(map(collection_list_cleaner, data))

    def get_collection_list_stats_dirty(self) -> Optional[List[Dict]]:
        url = SAAPIUrls.COLLECTION_STATS_LIST
        return self._get_request(url)

    def get_collection_list_stats(self) -> Optional[List[SACollectionStats]]:
        data = self.get_collection_list_stats_dirty()
        if data:
            return list(map(collection_list_stats_cleaner, data))
