from typing import List, Dict

from solapi.magic_eden.official_api.base import MagicEdenOfficialApi
from solapi.magic_eden.official_api.utils.consts import MEAPICollectionsUrlsBuilder
from solapi.magic_eden.official_api.utils.data import listing_response_mapper, activity_response_mapper, \
    collection_stats_mapper
from solapi.magic_eden.official_api.utils.types import MECollection, MEActivity, MECollectionStats
from solapi.utils.data import list_map


class MEListingItem(object):
    pass


class MagicEdenCollectionsApi(MagicEdenOfficialApi):
    url_builder_class = MEAPICollectionsUrlsBuilder
    url_builder: MEAPICollectionsUrlsBuilder

    def get_collections_dirty(self, offset: int = 0, limit: int = 100) -> List[Dict]:
        url = self.url_builder.collections(offset, limit)
        return self._get_request(url)

    def get_collections(self, offset: int = 0, limit: int = 100) -> List[MECollection]:
        return self.get_collections_dirty(offset, limit)

    def listings_dirty(self, symbol: str, offset: int = 0, limit: int = 100) -> List[Dict]:
        url = self.url_builder.listings(symbol, offset, limit)
        return self._get_request(url)

    def listings(self, symbol: str, offset: int = 0, limit: int = 100) -> List[MEListingItem]:
        dirty = self.listings_dirty(symbol, offset, limit)
        return list_map(listing_response_mapper, dirty)

    def activities_dirty(self, symbol: str, offset: int = 0, limit: int = 100) -> List[Dict]:
        url = self.url_builder.activities(symbol, offset, limit)
        return self._get_request(url)

    def activities(self, symbol: str, offset: int = 0, limit: int = 100) -> List[MEActivity]:
        dirty = self.activities_dirty(symbol, offset, limit)
        return list_map(activity_response_mapper, dirty)

    def stats_dirty(self, symbol: str) -> Dict:
        url = self.url_builder.stats(symbol)
        return self._get_request(url)

    def stats(self, symbol) -> MECollectionStats:
        dirty = self.stats_dirty(symbol)
        return None if dirty is None else collection_stats_mapper(dirty)
