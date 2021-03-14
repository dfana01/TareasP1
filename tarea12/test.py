import unittest
from main import fibonacci


class FibonacciTest(unittest.TestCase):
    def test_fib_0(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fib_1(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fib_2(self):
        self.assertEqual(fibonacci(2), 1)

    def test_fib_20(self):
        self.assertEqual(fibonacci(20), 6765)

    def test_fib_11(self):
        self.assertEqual(fibonacci(11), 89)


if __name__ == '__main__':
    unittest.main()
