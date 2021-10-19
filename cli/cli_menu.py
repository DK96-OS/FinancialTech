from typing import Optional

from cli.database.new_database import determine_database_attributes


def print_main_menu_options():
    """ The main menu options are printed out """
    print("=== Main Menu Options ===")
    print("-------------------------")
    print("1 : Create a new Database")
    print("2 : Load Database from a File")
    print("3 : Create a new Journal")
    print("4 : Load Journal from a File")
    print("_________________________")


def create_new_database() -> bool:
    """ Initialize a new database file """
    db_attrs = determine_database_attributes()
    if db_attrs is None:
        return False
    # Todo: Create the database file, or wait
    #   How will the data be structured
    # Todo: Discard data in memory, if associated with an existing database
    #   Determine if the data contains changes that should be saved
    #   Prompt saving changes if appropriate
    print("Failed to create new database")
    return False


def load_database_from_file() -> bool:
    """ Load a database from a file """
    # Todo: Obtain the file to load
    #   Open a file picker dialog, wait for a selection
    #   Determine if the file needs to be decoded or read in a specific way
    #   Load the file into memory
    print("Failed to load database - not implemented yet")
    return False


def create_new_journal() -> bool:
    """ Create a new Journal """
    from cli.journal.new_journal import determine_journal_attributes
    journal_attrs = determine_journal_attributes(True)
    if journal_attrs is None:
        return False
    # Todo: Create Journal File

    from cli.journal.cli_journal_menu import print_journal_menu
    print_journal_menu()

    return True


def load_journal() -> bool:
    """ Load a Journal from a file """

    # Todo: Find the file and open it
    # Todo: Validate the Journal data
    return False


def write_to_file() -> bool:
    """  """
    # Todo: Check data present in memory
    #   Determine if present data was obtained from an existing file
    #
    print("Failed to write to file - not implemented yet")
    return False


def process_menu_selection(input_str: str) -> Optional[bool]:
    """ Process the input, initiate the corresponding action """
    if input_str == "1":
        return create_new_database()
    elif input_str == "2":
        return load_database_from_file()
    elif input_str == "3":
        return create_new_journal()
    elif input_str == "4":
        return load_journal()
    else:
        return None
