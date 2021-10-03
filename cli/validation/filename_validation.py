""" Validation for Filenames """


def is_valid_filename(string: str) -> bool:
    """ Determines whether the given string is a valid filename """
    if not isinstance(string, str):
        return False
    if len(string) >= 100:
        return False
    # Todo: Provide checks on character set
    return True
