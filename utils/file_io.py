"""
TODO:
"""

def read_lines(filepath: str, newlines: bool = True) -> list[str]:
    """
    TODO:
    """
    # Init vars.
    contents: list[str] = []

    # Open source file and consume contents.
    with open(filepath, 'r') as file:
        if newlines:
            contents = file.readlines()
        else:
            contents = file.read().splitlines()
        file.close()

    # Forward source to caller.
    return contents
