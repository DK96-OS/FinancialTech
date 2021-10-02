

def check_exit():
    """ Determines whether to exit the program """
    print("\n\tType n, q, or e to close the program: ")
    cli_input = input()
    return cli_input in ("n", "q", "e")
