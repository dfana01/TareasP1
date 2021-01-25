import unittest
from problems import counting_valleys


class TestCountingValleysTestFact(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(counting_valleys.countingValleys(8, "UDDDUDUU") == 1)

    def test_case_2(self):
        self.assertTrue(counting_valleys.countingValleys(12, "DDUUDDUDUUUD") == 2)


if __name__ == '__main__':
    unittest.main()
