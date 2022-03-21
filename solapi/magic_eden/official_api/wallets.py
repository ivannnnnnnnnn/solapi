from typing import List, Dict

from solapi.magic_eden.official_api.base import MagicEdenOfficialApi
from solapi.magic_eden.official_api.utils.consts import MEAPIWalletUrlsBuilder
from solapi.magic_eden.official_api.utils.data import token_response_mapper, activity_response_mapper, \
    offer_response_mapper, \
    escrow_balance_response_mapper
from solapi.magic_eden.official_api.utils.types import MEActivity, METoken, MEOffer, MEEscrowBalance
from solapi.utils.data import list_map


class MagicEdenWalletsApi(MagicEdenOfficialApi):
    url_builder_class = MEAPIWalletUrlsBuilder
    url_builder: MEAPIWalletUrlsBuilder

    def tokens_dirty(self, wallet_address: str, offset: int = 0, limit: int = 100,
                     listed_only: bool = False) -> List[Dict]:
        url = self.url_builder.tokens(wallet_address, offset, limit, listed_only)
        return self._get_request(url)

    def tokens(self, wallet_address: str, offset: int = 0, limit: int = 100,
               listed_only: bool = False) -> List[METoken]:
        dirty = self.tokens_dirty(wallet_address, offset, limit, listed_only)
        return list_map(token_response_mapper, dirty)

    def activities_dirty(self, wallet_address: str, offset: int = 0, limit: int = 100) -> List[Dict]:
        url = self.url_builder.activities(wallet_address, offset, limit)
        return self._get_request(url)

    def activities(self, wallet_address: str, offset: int = 0, limit: int = 100) -> List[MEActivity]:
        dirty = self.activities_dirty(wallet_address, offset, limit)
        return list_map(activity_response_mapper, dirty)

    def offers_made_dirty(self, wallet_address: str, offset: int = 0, limit: int = 100) -> List[Dict]:
        url = self.url_builder.offers_made(wallet_address, offset, limit)
        return self._get_request(url)

    def offers_made(self, wallet_address: str, offset: int = 0, limit: int = 100) -> List[MEOffer]:
        dirty = self.offers_made_dirty(wallet_address, offset, limit)
        return list_map(offer_response_mapper, dirty)

    def offers_received_dirty(self, wallet_address: str, offset: int = 0, limit: int = 100) -> List[Dict]:
        url = self.url_builder.offers_received(wallet_address, offset, limit)
        return self._get_request(url)

    def offers_received(self, wallet_address: str, offset: int = 0, limit: int = 100) -> List[MEOffer]:
        dirty = self.offers_received_dirty(wallet_address, offset, limit)
        return list_map(offer_response_mapper, dirty)

    def escrow_balance_dirty(self, wallet_address: str) -> Dict:
        url = self.url_builder.escrow_balance(wallet_address)
        return self._get_request(url)

    def escrow_balance(self, wallet_address: str) -> MEEscrowBalance:
        dirty = self.escrow_balance_dirty(wallet_address)
        if dirty:
            return escrow_balance_response_mapper(dirty)
