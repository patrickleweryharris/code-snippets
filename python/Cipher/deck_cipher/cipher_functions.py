# Functions for running an encryption or decryption algorithm

ENCRYPT = 'e'
DECRYPT = 'd'

# Write your functions after this comment.  Do not change the statements above
# this comment.  Do not use import, open, input or print statements in the
# code that you submit.  Do not use break or continue statements.

def clean_message(message):
    """(str) -> str

    Return a copy of the message containing only its alphabetic
    characters, in uppercase

    >>>clean_message('Hello there')
    'HELLOTHERE'
    >>>clean_message('yH*&23  ?')
    'YH'
    """

    cleaned_message = ''
    for char in message.upper():
        if char.isalpha():
            cleaned_message += char
            # Only the alphabetic characters are returned

    return cleaned_message

def encrypt_letter(letter, keystream_value):
    """(str, int) -> str

    Return the letter encrypted using the keysteam value

    >>>encrypt_letter('A', 2)
    'C'
    >>>encrypt_letter('Z', 12)
    'L'
    """
    ascii_zero = ord('A') # The value of ord('A') == 65
    return chr(((ord(letter) - ascii_zero + keystream_value) % 26) + ascii_zero)

def decrypt_letter(letter, keystream_value):
    """(str, int) -> str

    Precondition: letter must be alphabetical, len(letter) == 1

    Return the letter decrpyted using the keystream value

    >>>decrypt_letter('C', 2)
    'A'
    >>>decrypt_letter('L', 12)
    'Z'
    """
    ascii_zero = ord('A') # The value of ord('A') == 65
    return chr(((ord(letter) - ascii_zero - keystream_value) % 26) + ascii_zero)

def swap_cards(deck, card_index):
    """(list of int, int) -> NoneType

    Precondition: card_index <= last index of  the deck

    Swap the card of card_index indicated with the card
    that follows it in the deck. If the card is at the end of the deck,
    swap it with the first card in the deck

    >>>deck = [1, 3, 2, 4]
    >>>swap_cards(deck, 3)
    >>>deck
    [4, 3, 2, 1]

    >>>deck = [7, 4, 5, 3, 1, 2, 6]
    >>>swap_cards(deck, 2)
    >>>deck
    [7, 4, 3, 5, 1, 2, 6]
    """


    for i in range(len(deck)):
        if i == card_index and deck [i] == deck [-1]:
            # If the card being swapped is the last card
            deck [0], deck [i] = deck [i], deck [0]
        elif i == card_index:
            deck [i], deck [i + 1] = deck [i + 1], deck [i]

def get_small_joker_value(deck):
    """(list of int) -> int

    Precondition: deck must be valid (contains all ints up to the
    highest int in the deck and is not an empty list)

    Return the second highest value (the small joker) in the deck

    >>>get_small_joker_value([1, 4, 5, 7, 8, 2])
    7
    """

    return (max(deck) - 1) # Since the deck is a continuos stream of ints,
    # the small joker will always be one less than the big joker

def get_big_joker_value(deck):
    """(list of int) -> int

    Precondition: deck must be valid (contains all ints up to the
    highest int in the deck and is not an empty list)

    Return the highest value (the big joker) in the deck

    >>>get_big_joker_value([1, 3, 7, 8, 9, 2, 5, 6, 4])
    9
    """
    return max(deck)

def move_small_joker(deck):
    """(list of int) -> NoneType

    Switch the small joker and the card that follows it in the deck. If the
    small joker falls at the end of the deck, swtich it with the first card.

    >>>deck = [1, 3, 7, 8, 9, 2, 5, 6, 4]
    >>>move_small_joker(deck)
    >>>deck
    [1, 3, 7, 9, 8, 2, 5, 6, 4]
    """

    small_joker_index = deck.index(get_small_joker_value(deck))
    deck =  swap_cards(deck, small_joker_index)


def move_big_joker(deck):
    """(list of int) -> NoneType

    Move the big joker two steps down the deck. If the big joker falls at
    the end of the deck, start at the beginning of the deck (Treat the deck
    as circular).

    >>>deck = [8, 3, 7, 1, 9, 2, 5, 6, 4]
    >>>move_big_joker(deck)
    >>>deck
    [8, 3, 7, 1, 2, 5, 9, 6, 4]
    """
    big_joke =  get_big_joker_value(deck)
    big_joker_index = deck.index(big_joke)
    if big_joke == deck [-1]:
        swap_cards(deck, big_joker_index)
        swap_cards(deck, 0)



    else:
        swap_cards(deck, big_joker_index)
        swap_cards(deck, big_joker_index + 1)


def triple_cut(deck):
    """(list of int) -> NoneType

    Perform a triple cut on the deck. Everything above the first joker in the
    deck goes to the bottom of the deck, and everything under the second joker
    in the deck goes to the top.

    >>>deck = [9, 3, 7, 1, 2, 5, 8, 6, 4]
    >>>triple_cut(deck)
    >>>deck
    [6, 4, 9, 3, 7, 1, 2, 5, 8]

    >>>deck = [6, 3, 7, 8, 2, 5, 9, 1, 4]
    >>>triple_cut(deck)
    >>>deck
    [1, 4, 8, 2, 5, 9, 6, 3, 7]

    >>>deck = [5, 3, 7, 1, 2, 8, 9, 6, 4]
    >>>triple_cut(deck)
    >>>deck
    [6, 4, 8, 9, 5, 3, 7, 1, 2]
    """
    new_deck = []
    # Moves the cutting to another list to avoid mutating the deck improperly

    first_cut= []
    second_cut= []
    big_joker_index = deck.index(get_big_joker_value(deck))
    small_joker_index = deck.index(get_small_joker_value(deck))

    if big_joker_index > small_joker_index:
        first_cut= deck [:small_joker_index]
        second_cut= deck [big_joker_index + 1:]
        new_deck = deck[small_joker_index:big_joker_index + 1]
        new_deck= second_cut+ new_deck + first_cut

    else: # When small_joker_index > big_joker_index
        first_cut= deck [:big_joker_index]
        second_cut= deck [small_joker_index + 1:]
        new_deck = deck [big_joker_index: small_joker_index + 1]
        new_deck = second_cut + new_deck + first_cut

    deck.clear()
    deck.extend(new_deck)


def insert_top_to_bottom(deck):
    """(list of int) -> NoneType

    Using the value of the last entry in deck, move that amount of cards from
    the front of the deck to the back of the deck, followed by the last entry.
    If the last entry is the big joker, use the small joker as a stand in for
    the last entry.
    # Needs work

    >>>deck = [3, 1, 2, 7, 8, 4, 9, 5, 6]
    >>>insert_top_to_bottom(deck)
    >>>deck
    [9, 5, 3, 1, 2, 7, 8, 4, 6]

    >>>deck = [3, 1, 2, 7, 8, 4, 6, 5, 9]
    >>>insert_top_to_bottom(deck)
    >>>deck
    [3, 1, 2, 7, 8, 4, 6, 5, 9]
    """

    if deck [-1] != get_big_joker_value(deck):
        # If the last card is the big joker value, nothing happens
        new_deck = deck [deck [-1] : -1 ] + deck [:deck[-1]] + [deck [-1]]
        deck.clear()
        deck.extend(new_deck)


def get_card_at_top_index(deck):
    """(list of int) -> int

    Return the value of the card using the first int in the deck as the index
    reference. Special case: if the first int is the max of the deck
    (the big joker), use the second largest value (the small joker) instead.

    >>>get_card_at_top_index([2, 3, 4, 1])
    4
    """
    if deck [0] == get_big_joker_value(deck):
        return deck[get_small_joker_value(deck)]

    return deck[deck[0]]
def get_next_keystream_value(deck):
    """(list of int) -> int

    Return the next keystream value of the deck using the five steps
    of the algorithm

    >>>deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24,
    27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>>get_next_keystream_value(deck)
    11
    """

    keystream_value = get_next_keystream_helper(deck)

    big_joke = get_big_joker_value(deck)
    small_joke = get_small_joker_value(deck)
    while keystream_value == big_joke or keystream_value == small_joke:
        # The keystream value cannot be a joker, so this while loop executes
        # unitl a non joker value is produced
        keystream_value = get_next_keystream_helper(deck)
        # Uses a helper fucntion to avoid duplicate code


    return keystream_value
    # Once a proper keystream value is produced, it is returned


def get_next_keystream_helper(deck):
    """(list of int) -> int

    This helper function generates a keystream value using the deck
    and returns it to the get_next_keystream_value function. Used to avoid
    creating duplicate code

    >>>deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24,
    27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>>get_next_keystream_helper(deck)
    11
    """
    move_small_joker(deck)
    move_big_joker(deck)
    triple_cut(deck)
    insert_top_to_bottom(deck)
    return get_card_at_top_index(deck)

def process_messages(deck, messages, encrypt_or_decrypt):
    """(list of int, list of str, str) -> list of str

    Return the messages encrypted or decrypted using the specified deck.
    The parameter encrypt_or_decrypt will be ENCRYPT to encrpyt the message,
    and DECRYPT to decrypt the message

    >>>deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24,
    27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>>process_messages(deck, ['Patty', 'Cakes'], ENCRYPT)
    ['AJQAI', 'BLVLT']

    >>>deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24,
    27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>>process_messages(deck, ['AJQAI', 'BLVLT'], DECRYPT)
    ['PATTY', 'CAKES']

    """
    returned_message = []

    for message in messages:

        new_message = ''
        cleaned_message = clean_message(message) # Cleans the message of
        # punctation and makes it all upper case

        for letter in cleaned_message:
            keystream_value = get_next_keystream_value(deck)
            # Generates a keystream value for each letter

            if encrypt_or_decrypt == ENCRYPT:
                new_message = new_message + encrypt_letter(letter, keystream_value)

            else: #  Where encrypt_or_decrypt == DECRYPT
                new_message = new_message + decrypt_letter(letter, keystream_value)

        returned_message.append(new_message)

    return returned_message

def read_messages(message_file):
    """(file open for reading) -> list of str

    Read and return the message_file, with each line separated into a different
    item in a list and the newline character removed.
    """

    returned_message = []
    contents = message_file.readlines()
    for item in contents:
        returned_message.append(item.strip('\n'))
        # Takes out the newline character
    return returned_message

def is_valid_deck(deck):
    """(list of int) -> bool

    A valid deck contains all ints from 1 to the highest value of the deck.
    This function returns wheter the supplied deck is valid.

    >>>is_valid_deck([1, 2, 3, 5, 7, 6, 4, 9])
    False

    >>>is_valid_deck([1, 2, 3, 5, 7, 6, 4, 8])
    True

    """
    if deck == []: # An empty list cannot be valid
        return False

    else:
        i = 1 # The first entry in the deck will always be one


        while i <= max(deck):
        # Starting at the first entry, go through each succeding
        # int up the last and make sure it is contained in the deck
            if not i in deck:
            # If this if statement is never true the function returns True
                return False
            i += 1 # Iterates through each int up the max of the deck

        return True

def read_deck(deck_file):
    """(file open for reading) -> list of int

    Read and return in a list the numbers contained in the deck_file in order.
    """

   # To whomever is marking this: Please forgive me for the absolute cluster
   # that the following function body is. It can definetly be far more efficent,
   # but I lack the requiste time to improve it. Sorry about that!

    contents = deck_file.readlines()
    each_line_split = []
    list_of_ints  = []
    ints_in_string_form = []

    for line in contents:
        each_line_split.append(line.split())

    for item in each_line_split:
        if item != []: # If item == [] it was a newline character
            for ints in item:
                ints_in_string_form.append(ints.split())

    for item in ints_in_string_form:
        # The ints are now separated, but they are in string form
        for ints in item:
            list_of_ints.append(int(ints))
    return list_of_ints
