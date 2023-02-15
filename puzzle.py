""" Puzzle module
Module checks table 9x9
https://github.com/MartaSamoilenkoPn/Lecture0.git
"""

def validate_board(board : list) -> bool:
    """
    >>> validate_board([\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"\
])
    False
    >>> validate_board([\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   2  **",\
 "  8  2***",\
 "  2  ****"\
])
    True
    """
    if len(board) < 9 :
        return False
    for column_index in range(5):
        number_list = []
        for carry in range(5):
            if board[8 - column_index - carry][column_index] not in [' ', '*'] and\
                board[8 - column_index - carry][column_index] not in number_list:
                number_list.append(board[8 - column_index - carry][column_index])
            elif board[8 - column_index - carry][column_index] not in [' ', '*']:
                return False
        for carry in range(1, 5):
            if board[8 - column_index][column_index + carry] not in [' ', '*'] and\
                board[8 - column_index][column_index + carry] not in number_list:
                number_list.append(board[8 - column_index][column_index + carry])
            elif board[8 - column_index][column_index + carry] not in [' ', '*']:
                return False
    for column_index in range(9):
        number_list = []
        for line_index in range(9):
            if board[line_index][column_index] not in [' ', '*'] and\
                board[line_index][column_index] not in number_list:
                number_list.append(board[line_index][column_index])
            elif board[line_index][column_index] not in [' ', '*']:
                return False
    return True

if __name__ == "__main__" :
    import doctest
    print(doctest.testmod())
