import unittest
import cipher_functions as a2

FAILURE_MESSAGE = '''
read_deck failed.
  Test case description: {0}
  argument: file with contents {1}
  expected return value: {2}
  actual return value: {3}
'''

# the deck from the handout
deck_handout = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21,
                24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]


class TestReadDeck(unittest.TestCase):

    def run_test(self, p1, expected, desc):
        file_contents = repr(p1.getvalue())
        returned = a2.read_deck(p1)
        msg = FAILURE_MESSAGE.format(desc, file_contents, expected, returned)
        self.assertEqual(returned, expected, msg)

    
    def test_01_read_deck_handout(self):
        import io
        deck1 = io.StringIO(
            '''1 4 7 10 13 16 19 22 25
28 3 6 9 12 15 18 21 24
27 2 5 8 11 14 17 20 23 26
''')
        expected = deck_handout[:]
        desc = 'deck from handout'
        self.run_test(deck1, expected, desc)


 
if __name__ == '__main__':
    unittest.main()
