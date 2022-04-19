from cli.cli_menu import process_menu_selection, print_main_menu_options
from cli.cli_shutdown import check_exit

print("Welcome to Financial Tech!")

MAIN_MENU_LOOP = True


def show_main_menu() -> bool:
    """ Prints the menu, waits for an input and processes it
    :returns True if the selection was handled successfully
    """
    print_main_menu_options()
    cli_input = input("What would you like to do?\n")
    task_result = process_menu_selection(cli_input)
    if task_result is None:
        print("Input not recognized")
        return False
    elif task_result:
        print("Task Complete!")
        return True
    else:
        print("Task Failed...")
        return False


while MAIN_MENU_LOOP:
    menu_result = show_main_menu()
    if not menu_result and check_exit():
        MAIN_MENU_LOOP = False

# Todo: Clean up any data remaining in memory
#  The program is about to exit
