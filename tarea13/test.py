import unittest
from main import *


class Test(unittest.TestCase):
    def test(self):
        main()
        self.assertEqual(1,1)


if __name__ == '__main__':
    unittest.main()
