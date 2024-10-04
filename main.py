"""
TODO:
"""

from compiler.tokenize import tokenize

def main() -> None:
    """
    TODO:
    """
    for token in tokenize("main.arf"):
        print(token.lexeme, token.type)

if __name__ == "__main__":
    main()
