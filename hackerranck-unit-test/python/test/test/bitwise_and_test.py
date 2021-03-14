import unittest

from problems.bitwise_and import bitwise_and


class Test(unittest.TestCase):
    def test_case_1_poisonous_plants(self):
        self.assertEqual(bitwise_and(5, 2), 1)

    def test_case_2_poisonous_plants(self):
        self.assertEqual(bitwise_and(8, 5), 4)

    def test_case_3_poisonous_plants(self):
        self.assertEqual(bitwise_and(2, 2), 0)


if __name__ == '__main__':
    unittest.main()
