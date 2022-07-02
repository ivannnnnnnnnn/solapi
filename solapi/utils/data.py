from typing import List, Optional


def parse_str_status(status: str):
    """
    :param status: num in str (eg '1', '0')
    :return: bool
    """
    try:
        return bool(int(status))
    except ValueError:
        return False


def dict_get_recursive(d: dict, key: str, separator='.'):
    if not isinstance(key, str):
        raise TypeError(f'Expected `key` as `str` instance but get {type(key)}')
    path = key.split(separator)
    assert len(path) != 0, f'invalid key: {key}'
    current_key = path[0]
    if not isinstance(d, dict):
        raise TypeError(f'Expected `d` as `dict` instance but get {type(d)}')
    if len(path) == 1:
        return d.get(current_key, None)
    return dict_get_recursive(d.get(current_key, None), separator.join(path[1:]), separator)


def dict_get_recursive_safe(d: dict, key: str, separator='.'):
    try:
        return dict_get_recursive(d, key, separator)
    except:
        return None


def list_map(func, collection: Optional[List]):
    return None if collection is None else list(map(func, collection))
