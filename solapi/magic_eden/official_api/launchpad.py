from typing import List, Dict

from solapi.magic_eden.official_api.base import MagicEdenOfficialApi
from solapi.magic_eden.official_api.utils.consts import MEAPILaunchpadUrlsBuilder
from solapi.magic_eden.official_api.utils.data import launchpad_collection_mapper
from solapi.magic_eden.official_api.utils.types import MELaunchpadCollection
from solapi.utils.data import list_map


class MagicEdenLaunchpadApi(MagicEdenOfficialApi):
    url_builder_class = MEAPILaunchpadUrlsBuilder
    url_builder: MEAPILaunchpadUrlsBuilder

    def collections_dirty(self, offset: int = 0, limit: int = 100) -> List[Dict]:
        url = self.url_builder.collections(offset, limit)
        return self._get_request(url)

    def collections(self, offset: int = 0, limit: int = 100) -> List[MELaunchpadCollection]:
        dirty = self.collections_dirty(offset, limit)
        return list_map(launchpad_collection_mapper, dirty)
