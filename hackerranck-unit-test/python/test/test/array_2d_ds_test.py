import unittest
from problems import array_2d_ds


class TestHourglassSumTestFact(unittest.TestCase):
    def test_case_1(self):
        arr = [
            [1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 2, 4, 4, 0],
            [0, 0, 0, 2, 0, 0],
            [0, 0, 1, 2, 4, 0]
        ]
        self.assertTrue(array_2d_ds.hourglassSum(arr) == 19)

    def test_case_2(self):
        arr = [
            [1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 9, 2, -4, -4, 0],
            [0, 0, 0, -2, 0, 0],
            [0, 0, -1, -2, -4, 0]
        ]
        self.assertTrue(array_2d_ds.hourglassSum(arr) == 13)

    def test_case_3(self):
        arr = [
            [-9, -9, -9, 1, 1, 1],
            [0, -9, 0, 4, 3, 2],
            [-9, -9, -9, 1, 2, 3],
            [0, 0, 8, 6, 6, 0],
            [0, 0, 0, -2, 0, 0],
            [0, 0, 1, 2, 4, 0]
        ]
        self.assertTrue(array_2d_ds.hourglassSum(arr) == 28)


if __name__ == '__main__':
    unittest.main()
