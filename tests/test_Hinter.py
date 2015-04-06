import unittest
import sys
sys.path.append('..')
from Hinter import Hinter as H

class TestGetGuessHint(unittest.TestCase):
    def test_zero_position(self):
        self.assertEqual(H('obbr').getHint('borg', True), (3,0))
        self.assertEqual(H('bgyo').getHint('oygb', True), (4,0))

    def test_zero_color(self):
        self.assertEqual(H('oygp').getHint('rrbb', True), (0,0))

    def test_mixed(self):
        self.assertEqual(H('rrpb').getHint('bypr', True), (2,1))
        self.assertEqual(H('yogb').getHint('boyg', True), (3,1))
        self.assertEqual(H('grop').getHint('prom', True), (1,2))
        self.assertEqual(H('prop').getHint('poor', True), (1,2))

    def test_exact(self):
        self.assertEqual(H('oygp').getHint('oygp', True), (0,4))

if __name__ == '__main__':
    unittest.main()
