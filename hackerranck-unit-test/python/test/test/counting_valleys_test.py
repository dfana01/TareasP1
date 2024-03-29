import unittest
from problems import counting_valleys


class TestCountingValleysTestFact(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(counting_valleys.counting_valleys(8, "UDDDUDUU") == 1)

    def test_case_2(self):
        self.assertTrue(counting_valleys.counting_valleys(12, "DDUUDDUDUUUD") == 2)

    def test_case_3(self):
        self.assertTrue(counting_valleys.counting_valleys(0, "") == 0)

    def test_case_4(self):
        self.assertTrue(counting_valleys.counting_valleys(6, "DUDUDU") == 3)


if __name__ == '__main__':
    unittest.main()
