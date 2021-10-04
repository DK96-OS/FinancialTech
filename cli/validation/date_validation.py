""" Validates a Date """


def is_valid_date(string: str) -> bool:
    """ Determines whether this is a valid date
        The expected format is yyyy-mm-dd, the iso-format
    """
    if not isinstance(string, str):
        return False
    if len(string) != 10:
        return False
    if str.count(string, '-') != 2:
        return False
    return string.strip('-').isnumeric()
