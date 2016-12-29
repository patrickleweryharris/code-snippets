import tictactoe_functions
import builtins

# Get the initial value of the constant
constant_before = [tictactoe_functions.EMPTY]

# Type check and simple test for tictactoe_functions.is_between
result = tictactoe_functions.is_between(2, 1, 3)
assert isinstance(result, bool), \
       'tictactoe_functions.is_between should return a bool, but returned ' \
       '{0}'.format(type(result))
assert result, \
       'tictactoe_functions.is_between(2, 1, 3) should return True, but ' \
       'returned {0}.'.format(result)

# Type check and simple test for tictactoe_functions.game_board_full
result = tictactoe_functions.game_board_full('----')
assert isinstance(result, bool), \
       'tictactoe_functions.game_board_full should return a bool, but ' \
       'returned {0}.'.format(type(result))
assert not result, \
       "tictactoe_functions.game_board_full('----') should return False, " \
       'but returned {0}.'.format(result)

# Type check and simple test for tictactoe_functions.get_board_size
result = tictactoe_functions.get_board_size('-')
assert isinstance(result, int), \
       'tictactoe_functions.get_board_size should return an int, but ' \
       'returned {0} .'.format(type(result))
assert result == 1, \
       "tictactoe_functions.get_board_size('-') should return 1, but "\
       'returned {0}.'.format(result)

# Type check and simple test for tictactoe_functions.make_empty_board
result = tictactoe_functions.make_empty_board(1)
assert isinstance(result, str), \
       'tictactoe_functions.make_empty_board should return a str, but ' \
       'returned {0}.'.format(type(result))
assert result == constant_before[0], \
       "tictactoe_functions.make_empty_board(1) should return '" \
       + constant_before[0] + "', but returned '{0}'.".format(result)

# Type check and simple test for tictactoe_functions.get_position
result = tictactoe_functions.get_position(1, 1, 3)
assert isinstance(result, int), \
       'tictactoe_functions.get_position should return an int, but returned ' \
       '{0}.'.format(type(result))
assert result == 0, \
       'tictactoe_functions.get_position(1, 1, 3) should return 0, but ' \
       'returned {0}.'.format(result)

# Type check and simple test for tictactoe_functions.make_move
result = tictactoe_functions.make_move('X', 1, 1, '-')
assert isinstance(result, str), \
       'tictactoe_functions.make_move should return a str, but returned {0}.' \
       .format(type(result))
assert result == 'X', \
       "tictactoe_functions.make_move('X', 1, 1, '-') should return 'X', "\
       "but returned '{0}'.".format(result)

# Type check and simple test for tictactoe_functions.extract_line
result = tictactoe_functions.extract_line('abcd', 'across', 1)
assert isinstance(result, str), \
       "tictactoe_functions.extract_line('abcd', 'across', 1) should return " \
       'a str, but returned {0}.'.format(type(result))
assert result == 'ab', \
       "tictactoe_functions.extract_line('abcd', 'across', 1) should return " \
       "'ab', but returned '{0}'.".format(result)

result = tictactoe_functions.extract_line('abcd', 'down', 1)
assert isinstance(result, str), \
       "tictactoe_functions.extract_line('abcd', 'down', 1) should return " \
       'a str, but returned {0}.'.format(type(result))
assert result == 'ac', \
       "tictactoe_functions.extract_line('abcd', 'down', 1) should return " \
       "'ac', but returned '{0}'.".format(result)

result = tictactoe_functions.extract_line('abcd', 'up_diagonal', 1)
assert isinstance(result, str), \
       "tictactoe_functions.extract_line('abcd', 'up_diagonal', 1) should " \
       'return a str, but returned {0}.'.format(type(result))
assert result == 'cb', \
       "tictactoe_functions.extract_line('abcd', 'up_diagonal', 1) should " \
       "return 'cb', but returned '{0}'.".format(result)

result = tictactoe_functions.extract_line('abcd', 'down_diagonal', 1)
assert isinstance(result, str), \
       "tictactoe_functions.extract_line('abcd', 'down_diagonal', 1) should " \
       'return a str, but returned {0}.'.format(type(result))
assert result == 'ad', \
       "tictactoe_functions.extract_line('abcd', 'down_diagonal', 1) should " \
       "return 'ad', but returned '{0}'.".format(result)

# Get the final values of the constants
constant_after = [tictactoe_functions.EMPTY]

# Check whether the constants are unchanged.
assert constant_before == constant_after, \
       '''Your function(s) modified the value of constant EMPTY.
       Edit your code so that the value of this constant is not 
       changed by your functions.'''
    

print("""

Yippee! The simple checker program completed without error.

This means that the functions in tictactoe_functions.py:
- are named correctly,
- take the correct number of arguments, 
- return the correct types, and
- work in one simple case

This does NOT mean that the functions are correct!

Be sure to thoroughly test your functions yourself before submitting.""")


# Check for use of functions print and input.

def disable_print(*args):
    raise Exception("You must not call built-in function print!")

def disable_input(*args):
    raise Exception("You must not call built-in function input!")

builtins.print = disable_print
builtins.input = disable_input
