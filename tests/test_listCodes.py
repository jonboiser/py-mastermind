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
        self.assertEqual(LC('roygp', 0), [])

    def test_simple_alphabet(self):
        self.assertEqual(LC('roy',1), ['r','o','y'])
        self.assertEqual(LC('ab',2), ['aa', 'ab', 'ba', 'bb'])

    def test_large_outputs(self):
        self.assertEqual(len(LC('abcde', 5)), 5**5)

if __name__ == '__main__':
    unittest.main()
