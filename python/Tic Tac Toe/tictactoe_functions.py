import math

EMPTY = '-'

def is_between(value, min_value, max_value):
    """ (number, number, number) -> bool

    Precondition: min_value <= max_value

    Return True if and only if value is between min_value and max_value,
    or equal to one or both of them.

    >>> is_between(1.0, 0.0, 2)
    True
    >>> is_between(0, 1, 2)
    False
    """

    # Students are to complete the body of this function, and then put their
    # solutions for the other required functions below this function.
    
    return min_value <= value <= max_value

def game_board_full(game_board):
    """(str) -> bool

    Precondition: game_board must be of appropriate length (i.e the game board must be a square), and composed of only valid characters ('X', 'O', or EMPTY)

    Return True iff game_board has no EMPTY characters

    >>> game_board_full('xoxoox-x-')
        False
    >>> game_board_full('oxoxxoxox')
        True
    """

    return not (EMPTY in game_board)

def get_board_size(game_board):
    """(str) -> int

    Precondition: board_size is a perfect square

    Return the side length of the tic tac toe board

    >>>get_board_size('x-ox')
    2
    >>>get_board_size('xoxoxxoxx')
    3
    """

    return int(math.sqrt(len(game_board))) # Had to use int() because the result of math.sqrt() is a float

def make_empty_board(board_size):
    """(int) -> str

    Precondition: board_size must be of valid length (i.e. an int between 1 and 9)

    Return a string showing that the board of side length board_size is currently empty, with no x's or o's being chosen yet (i.e. every character is EMPTY)

    >>>make_empty_board(2)
    '----'
    >>>make_empty_board(3)
    '---------'
    """

    return EMPTY * (board_size ** 2)

def get_position(row_index, col_index, board_size):
    """(int, int, int) -> int

    Return the str_index of the cell in the game board of size board_size within the row, row_index, and the column, col_index

    >>>get_position(1, 1, 2)
    0
    >>>get_position(3, 2, 3)
    7
    """

    return (row_index - 1) * board_size + col_index - 1 # Using a formula given in the assignment brief to get the string index number

def make_move(move, row_index, col_index, game_board):
    """(str, int, int, str) -> str

    Precondition: The move made must be valid (i.e. must be either an 'X' or an 'O'), made in an unused location 

    Return the game_board after a move is made, assigning whatever string the move is to the str_index indicated by row_index, col_index # ~~Reword this

    >>>make_move('X', 1, 1, '---------')
    'X--------'
    >>>make_move('O', 3, 2, '---X--O-O')
    '---X--OOO)'
    """
    index_num = get_position(row_index, col_index, get_board_size(game_board)) # Using a variable so the following line is less cluttered
    return game_board [0:index_num] + move + game_board [index_num + 1:]

def extract_line(game_board, direction, row_or_column):
    """(str, str[, int]) -> str

    Precondition: game_board must be valid, containing the specified row or column.

    Return the characters that make up the specfied row, column or diagonal in the given game board. When requesting a diagonal, the row_or_column number is irrelevant

    >>>extract_line('---X--O-O', 'across', 3)
    'O-O'
    >>>extract_line('OXOXOXOXO', 'down', 2)
    'XOX'
    >>>extract_line('OXOXOXOXO', 'up_diagonal', 1)
    'OOO'
    >>>extract_line('OXOXOXOXO', 'down_diagonal', 1)
    'OOO'
    """

    board_size = get_board_size(game_board) # Using a variable to represent get_board_size(game_board) so the code below is less cluttered

    if direction == 'across':
        return game_board [get_position(row_or_column, 1, board_size): get_position(row_or_column, board_size, board_size) + 1] # Using get_position to grab the index of the first value, then the index of the second value

    elif direction == 'down':
        return game_board [get_position(1, row_or_column, board_size): get_position(board_size, board_size, board_size) + 1: board_size] # Using get_position to grab the index of the first value, then using a stride length to skip to the next value in the column

    elif direction == 'up_diagonal':
        diagonal_string =  game_board[get_position(1, board_size, board_size): (get_position(board_size, 1, board_size) + 1): board_size - 1]
        return diagonal_string [::-1] # Flips the string, because the str 'diagonal_string' is backwards

    else: # This is where direction == 'down_diagonal'
        return game_board[get_position(1, 1, board_size):: board_size + 1] # The second argument can be blank because this goes to the end of the string
    # The elif and else statements for 'up_diagonal' and 'down_diagonal' only use two of the parameters, because the row or column number is irrelevant
