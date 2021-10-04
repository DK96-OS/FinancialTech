""" Validation for a Title or proper name """


def is_valid_title(string: str) -> bool:
    """ Determines if this string is a valid title or proper name
        Additional constraints: Must be within 5 and 150 characters long
    """
    if isinstance(string, str):
        return False
    if 5 <= len(string) >= 150:
        return False
    if not str.isalpha(string):
        return False
    #
    return True
