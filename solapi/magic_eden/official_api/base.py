from typing import Type

from solapi.magic_eden.official_api.utils.consts import MEUrlBuilder
from solapi.magic_eden.official_api.utils.types import MagicEdenAPIEnvironment
from solapi.utils.api import BaseApi


class MagicEdenOfficialApi(BaseApi):
    url_builder_class: Type[MEUrlBuilder]
    url_builder: MEUrlBuilder

    def __init__(self, environment: MagicEdenAPIEnvironment = 'MAINNET'):
        self.url_builder = self.url_builder_class(environment)
