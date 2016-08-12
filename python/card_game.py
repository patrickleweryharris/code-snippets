"""
Luke has a unique deck of cards
Each card has a postitive three digit number printed on it.
There is exactly 1 card in the deck for every three digit postive integer
The cards are shuffled, and Luke pulls out a card
What is the probability that the card Luke pulls out will have a number whose
digits add to 15 on it?
"""


def card_game(trials):
    """(int) -> str

    Return the probability of a card being pulled from a deck of size (trials)
    having a three digit integer with digits adding to 15.

    >>> card_game(899)
    '7.67%'

    >>> card_game(60)
    '0.11%'
    """
    i = 0
    results = 0
    list_nums = list(range(100, 999))
    # Creates a list of all integers between 100 and 999

    while i < trials:
        first_digit = int(str(list_nums[i])[0])
        second_digit = int(str(list_nums[i])[1])
        third_digit = int(str(list_nums[i])[2])
        # Separates the digits of each integer into a string of that number,
        # then turns it back into an integer of just that number
        # e.g.: just takes the "1" of "100"

        if (first_digit + second_digit + third_digit) == 15:
            # Checks if the three numbers add to 15, if they do it adds 1 to
            # the results count
            results += 1
            probability = (results / 900) * 100
            # Finds the probability out of 900 options

        i += 1  # Tests until all 900 options have been exhausted

    return str(round(probability, 2)) + "%"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(card_game(899))
