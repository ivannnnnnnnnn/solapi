from typing import Dict, List

from solapi.magic_eden.official_api.base import MagicEdenOfficialApi
from solapi.magic_eden.official_api.utils.consts import MEAPITokensUrlBuilder
from solapi.magic_eden.official_api.utils.data import token_response_mapper, listing_response_mapper, \
    offer_response_mapper, activity_response_mapper
from solapi.magic_eden.official_api.utils.types import METoken, MEListingItem, MEOffer, MEActivity
from solapi.utils.data import list_map


class MagicEdenTokensApi(MagicEdenOfficialApi):
    url_builder_class = MEAPITokensUrlBuilder
    url_builder: MEAPITokensUrlBuilder

    def get_token_dirty(self, token: str) -> Dict:
        url = self.url_builder.get_token(token)
        return self._get_request(url)

    def get_token(self, token: str) -> METoken:
        dirty = self.get_token_dirty(token)
        if dirty:
            return token_response_mapper(dirty)

    def listings_dirty(self, token: str) -> List[Dict]:
        url = self.url_builder.listings(token)
        return self._get_request(url)

    def listings(self, token: str) -> List[MEListingItem]:
        dirty = self.listings_dirty(token)
        return list_map(listing_response_mapper, dirty)

    def offer_received_dirty(self, token: str, offset: int = 0, limit: int = 100) -> List[Dict]:
        url = self.url_builder.offer_received(token, offset, limit)
        return self._get_request(url)

    def offer_received(self, token: str, offset: int = 0, limit: int = 100) -> List[MEOffer]:
        dirty = self.offer_received_dirty(token, offset, limit)
        return list_map(offer_response_mapper, dirty)

    def activities_dirty(self, token: str, offset: int = 0, limit: int = 100) -> List[Dict]:
        url = self.url_builder.activities(token, offset, limit)
        return self._get_request(url)

    def activities(self, token: str, offset: int = 0, limit: int = 100) -> List[MEActivity]:
        dirty = self.activities_dirty(token, offset, limit)
        return list_map(activity_response_mapper, dirty)
