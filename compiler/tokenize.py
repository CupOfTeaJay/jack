"""
TODO:
"""

from enum import Enum
from utils.file_io import read_lines

class TokenType(Enum):
    """
    TODO:
    """
    # Unknown.
    NULL = 0

    # Literals.
    IDENTIFIER = 1
    STRING     = 2
    TYPE       = 3

    # Operators.
    ASSIGNMENT = 4

    # Delimiters.
    LEFT_CURLY   = 5
    LEFT_PAREN   = 6
    OCTOTHORPE   = 7
    RIGHT_CURLY  = 8
    RIGHT_PAREN  = 9
    SEMICOLON    = 10
    TRIPLE_QUOTE = 11

    # Keywords.
    ISO    = 12
    MUT    = 13
    RETURN = 14

class Token:
    """
    TODO:
    """
    def __init__(self, token_type: TokenType, lexeme: str):
        """
        TODO:
        """
        # Inject dependencies.
        self.type:   TokenType = token_type
        self.lexeme: str       = lexeme

def tokenize(source: str) -> list[Token]:
    """
    TODO:
    """
    # Init vars.
    tokens: list[Token] = []

    # ISO = 12
    # MUT = 13

    # Tokenize.
    for words in [line.split() for line in read_lines(source)]:
        for word in words:
            match word:
                case "{":
                    tokens.append(Token(TokenType.LEFT_CURLY, word))
                case "(":
                    tokens.append(Token(TokenType.LEFT_PAREN, word))
                case "#":
                    tokens.append(Token(TokenType.OCTOTHORPE, word))
                case "}":
                    tokens.append(Token(TokenType.RIGHT_CURLY, word))
                case ")":
                    tokens.append(Token(TokenType.RIGHT_PAREN, word))
                case ";":
                    tokens.append(Token(TokenType.SEMICOLON, word))
                case "\"\"\"":
                    tokens.append(Token(TokenType.TRIPLE_QUOTE, word))
                case "iso":
                    tokens.append(Token(TokenType.ISO, word))
                case "mut":
                    tokens.append(Token(TokenType.MUT, word))
                case "return":
                    tokens.append(Token(TokenType.RETURN, word))
                case _:
                    tokens.append(Token(TokenType.NULL, word))

    # Forward tokens to caller.
    return tokens
