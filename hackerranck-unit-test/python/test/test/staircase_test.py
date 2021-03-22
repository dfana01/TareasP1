import unittest

from problems.staircase import staircase

OUTPUT = "     #\n    ##\n   ###\n  ####\n #####\n######\n"


class Test(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(staircase(6), OUTPUT)


if __name__ == '__main__':
    unittest.main()
