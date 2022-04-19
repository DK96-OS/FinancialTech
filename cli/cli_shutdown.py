""" Handles CLI menu shutdown """


def check_exit() -> bool:
    """ Determines whether to exit the program """
    cli_input = input("\n\tType n, q, or e to close the program: ")
    return cli_input in ("n", "q", "e")


def check_close_submenu() -> bool:
    """ Determines whether the user wants to close the active menu """
    cli_input = input("\n\tType n, q, or e to close this submenu: ")
    return cli_input in ("n", "q", "e")
