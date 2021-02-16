import unittest

from problems.minimun_bribes import minimum_bribes


class MinimumBribesTest(unittest.TestCase):
    def test_case_1_minimum_bribes(self):
        self.assertEqual(minimum_bribes([2, 1, 5, 3, 4]), 3)

    def test_case_2_minimum_bribes(self):
        self.assertEqual(minimum_bribes([2, 5, 1, 3, 4]), "Too chaotic")

    def test_case_3_minimum_bribes(self):
        self.assertEqual(minimum_bribes([1, 2, 5, 3, 7, 8, 6, 4]), 7)

    def test_case_4_minimum_bribes(self):
        self.assertEqual(minimum_bribes([5, 1, 2, 3, 7, 8, 6, 4]), "Too chaotic")


if __name__ == '__main__':
    unittest.main()
