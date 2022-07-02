import abc
from http import HTTPStatus
from json.decoder import JSONDecodeError
from typing import Optional, Dict, Union, List

import requests

import logging

logger = logging.getLogger(__name__)


class BaseApi(abc.ABC):

    def _get_request(self, url: str) -> Union[Optional[Dict], Optional[List]]:
        r = requests.get(url)
        try:
            if r.status_code == HTTPStatus.OK:
                return r.json()
            logger.error(f'Request error. Status code: {r.status_code}')
        except JSONDecodeError as je:
            logger.error(f'Request error. Failed to parse json data. {str(je)}')
            return None
        except Exception as e:
            logger.error(f'Request error. {str(e)}')
