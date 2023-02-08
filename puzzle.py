""" Puzzle module

Module checks table 9x9

link
"""

def validate_board(board : list) -> bool:
    """
    >>> validate_board([
 "**** ****",
 "***1 ****",
 "**  3****",
 "* 4 1****",
 "     9 5 ",
 " 6  83  *",
 "3   1  **",
 "  8  2***",
 "  2  ****"
])
    False
    >>> validate_board([])
    False
    >>> validate_board([1])
    True
    """
    return None

if __name__ == "__main__" :
    import doctest
    doctest.testmod(verbose=True)
