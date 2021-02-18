import unittest

from problems.poisonous_plant import poisonous_plants


class Test(unittest.TestCase):
    def test_case_1_poisonous_plants(self):
        self.assertEqual(poisonous_plants([6, 5, 8, 4, 7, 10, 9]), 2)

    def test_case_2_poisonous_plants(self):
        self.assertEqual(poisonous_plants([3, 2, 5, 4]), 2)

    def test_case_3_poisonous_plants(self):
        self.assertEqual(poisonous_plants([4, 3, 7, 5, 6, 4, 2]), 3)


if __name__ == '__main__':
    unittest.main()
