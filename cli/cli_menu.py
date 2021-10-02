from typing import Optional


def print_main_menu_options():
    """ The main menu options are printed out """
    print("=== Main Menu Options ===")
    print("-------------------------")
    print("1 : Create a new database")
    print("2 : Load from a file")
    print("3 : Write to a file")
    print("_________________________")


def create_new_database() -> bool:
    """ Initialize a new database file """
    # Todo: Determine the attributes of the new database
    #   What is the name of the database
    #   How will the data be structured
    #   Will the data be encrypted
    # Todo: Discard data in memory, if associated with an existing database
    #   Determine if the data contains changes that should be saved
    #   Prompt saving changes if appropriate
    print("Failed to create new database - not implemented yet")
    return False


def load_from_file() -> bool:
    """ Load a database from a file """
    # Todo: Obtain the file to load
    #   Open a file picker dialog, wait for a selection
    #   Determine if the file needs to be decoded or read in a specific way
    #   Load the file into memory
    print("Failed to load database - not implemented yet")
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
        return load_from_file()
    elif input_str == "3":
        return write_to_file()
    else:
        return None
