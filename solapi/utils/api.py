import abc
from http import HTTPStatus
from json.decoder import JSONDecodeError
from typing import Optional, Dict

import requests


class BaseApi(abc.ABC):

    def _get_request(self, url: str) -> Optional[Dict]:
        r = requests.get(url)
        try:
            res = r.json()
            if r.status_code == HTTPStatus.OK and bool(res):
                return res
        except JSONDecodeError:
            return None
