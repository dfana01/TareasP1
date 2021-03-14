import unittest

from problems.nested_logic import nested_logic


class Test(unittest.TestCase):
    def test_case_1_poisonous_plants(self):
        self.assertEqual(nested_logic("9 6 2015", "6 6 2015"), 45)


if __name__ == '__main__':
    unittest.main()
