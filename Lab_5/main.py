import unittest
import sort
class Test_sort(unittest.TestCase):
    def test_1_1(self):
        self.assertEqual(sort.sort1([5, -9, 7, 1, -3]), [-9, 7, 5, -3, 1])
    def test_1_2(self):
        self.assertEqual(sort.sort2([7, -11, 13, 3, 2, 5, -8]), [13, -11, -8, 7, 5, 3, 2])
    def test_1_3(self):
        self.assertEqual(sort.sort3([15, 11,-2, -6, 12, 3, 8, 0]), [15, 12, 11, 8, -6, 3, -2, 0])