""" Determines whether a yes or no answer was provided """
from typing import Optional


def confirm_yes_or_no(string: str) -> Optional[bool]:
    """ Determines whether a yes or no action was provided
     :returns None if input is neither yes or no. True if yes.
    """
    if not isinstance(string, str):
        return None
    if len(string) > 3:
        return None
    lowercase_str = str.lower(string)
    if lowercase_str in ('y', 'yes'):
        return True
    if lowercase_str in ('n', 'no'):
        return False
