import unittest
import sys

sys.path.append('..')

from listCodes import listCodes as LC

class TestListCodes(unittest.TestCase):
    def trivialTest(self):
        pass

    def test_empty_input(self):
        self.assertEqual(LC({}, 5), [])
        self.assertEqual(LC((), 5), [])
        self.assertEqual(LC([], 5), [])
        self.assertEqual(LC('abc', 0), [])

    def test_simple_alphabet(self):
        self.assertEqual(LC('abc',1), ['a','b','c'])
        self.assertEqual(LC('ab',2), [('a','a'), ('a','b'), ('b','a'), ('b','b')])

    def test_large_outputs(self):
        self.assertEqual(len(LC(range(4), 10)), 4**10)

if __name__ == '__main__':
    unittest.main()
