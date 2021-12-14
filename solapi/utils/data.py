def parse_str_status(status: str):
    """
    :param status: num in str (eg '1', '0')
    :return: bool
    """
    try:
        return bool(int(status))
    except ValueError:
        return False
