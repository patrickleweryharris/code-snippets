import itertools
# This snippet has been turned into a full repo:
# github.com/patrickleweryharris/anagram_solver


def anagram_solver(lst):
    """
    Return all possible combinations of letters in lst

    @type lst: [str]
    @rtype: None
    """
    for i in range(0, len(lst) + 1):
        for subset in itertools.permutations(lst, i):
            possible = ''
            for letter in subset:
                possible += letter
            if len(possible) == len(lst):
                # itertools.permutations returns smaller lists
                print(possible)


if __name__ == '__main__':
    lst = ['o', 'r', 'y', 'a', 'n']
    anagram_solver(lst)
