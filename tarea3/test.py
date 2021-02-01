import unittest
from main import levenshtein_distance, calculate_close_pair, save_c


class TimeComparisonSet(unittest.TestCase):
    def test_levenshtein_distance(self):
        self.assertEqual(levenshtein_distance("abc", "abcasdf"), 6)

    def test_calculate_close_pair(self):
        self.assertEqual(calculate_close_pair([82, 69, 7, 31, 57]), (7, 57))

    def test_save_c(self):
        d = {}
        save_c(d, 'c1')
        self.assertEqual(d, {'c1': 1})


if __name__ == '__main__':
    unittest.main()
