import unittest
import sys
sys.path.append('..')
from getGuessHint import getGuessHint as hint

class TestGetGuessHint(unittest.TestCase):
    def test_zero_position(self):
        self.assertEqual(hint([5,1,0,3], [1,5,5,0], True), (3,0))
        self.assertEqual(hint([1,2,3,4], [4,3,2,1], True), (4,0))

    def test_zero_color(self):
        self.assertEqual(hint([1,2,3,4], [0,0,6,6], True), (0,0))

    def test_exact(self):
        self.assertEqual(hint([1,2,3,4], [1,2,3,4], True), (0, 4))

if __name__ == '__main__':
    unittest.main()
