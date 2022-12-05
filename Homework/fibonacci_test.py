import unittest
from lazy_fibonacci import fibonacci

class fibonacci_test(unittest.TestCase):
    def test_fib1(self):
        self.assertEqual(len(list(fibonacci(10))), 10)
        self.assertEqual(list(fibonacci(10)), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_fib2(self):
        res = fibonacci(4)
        self.assertEqual(next(res), 0)
        self.assertEqual(next(res), 1)
        self.assertEqual(next(res), 1)
        self.assertEqual(next(res), 2)

    def test_fib3(self):
        self.assertEqual(len(list(fibonacci(7))), 7)
        self.assertEqual(list(fibonacci(7)), [0, 1, 1, 2, 3, 5, 8])
