import unittest

from problems.plus_minus import plus_minus


class Test(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(plus_minus([-4, 3, -9, 0, 4, 1]), (0.500000, 0.333333, 0.166667))

    def test_case_2(self):
        self.assertEqual(plus_minus([1, 2, 3, -1, -2, -3, 0, 0]), (0.375000, 0.375000, 0.250000))


if __name__ == '__main__':
    unittest.main()
