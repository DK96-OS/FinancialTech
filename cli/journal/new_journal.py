""" Setup a new Journal """
import datetime
from typing import Optional

from cli.validation.confirm_option_validation import confirm_yes_or_no
from cli.validation.date_validation import is_valid_date
from cli.validation.filename_validation import is_valid_filename
from filesystem.journal_file_attributes import JournalFileAttributes
from model.journal.journal_attributes import JournalAttributes


def determine_journal_attributes(
        is_standalone: bool
) -> Optional[JournalAttributes]:
    """ Obtain the necessary journal attributes
    :param is_standalone If the Journal is saved as an independent file
    :returns An object containing Journal attributes
    """
    if is_standalone:
        cli_input = input("Journal Filename :")
        if is_valid_filename(cli_input):
            journal_filename = cli_input
        else:
            # Input was invalid. Abort
            return None
        cli_result = confirm_yes_or_no(input("Encrypt Journal? (y or n) :"))
        if cli_result is None:
            # Input was invalid. Abort
            return None
        if cli_result:
            # Todo: Determine Encryption parameters
            encryption_params = ('AES', 'GCM', '256')
        else:
            encryption_params = None
    else:
        journal_filename = None
        encryption_params = None
    # The remaining attributes apply to all Journals
    cli_input = input("Journal Title :")
    journal_title = cli_input
    #
    cli_input = input("Opening Date :")
    if is_valid_date(cli_input):
        open_date = datetime.date.fromisoformat(cli_input)
    else:
        return None
    #
    cli_input = input("Closing Date :")
    if is_valid_date(cli_input):
        close_date = datetime.date.fromisoformat(cli_input)
    else:
        return None
    return JournalFileAttributes(
        journal_filename, encryption_params,
        journal_title, open_date, close_date
    )
