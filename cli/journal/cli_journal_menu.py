""" The CLI menu that enables interaction with an open Journal """
from cli.cli_shutdown import check_close_submenu


def open_journal_menu():
    """ Start the Journal Menu loop """
    journal_menu_loop = True
    while journal_menu_loop:
        print_journal_menu()
        cli_input = input()
        menu_result = handle_journal_menu_selection(cli_input)
        if not menu_result:
            close_journal = check_close_submenu()
            if close_journal:
                journal_menu_loop = False
                # Todo: Save journal data


def print_journal_menu():
    """ Display the open Journal's menu """
    print("=== Journal Menu Options ===")
    print("----------------------------")
    print("1 : ")
    print("2 : ")
    print("3 : ")
    print("----------------------------")


def handle_journal_menu_selection(input_str: str) -> bool:
    """ Respond to the journal menu selection """
    if not str.isnumeric(input_str):
        return False
    if input_str == "1":
        # Todo:
        print("Unhandled")
    elif input_str == "2":
        # Todo:
        print("Unhandled")
    else:
        return False
    return True
