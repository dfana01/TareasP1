import unittest
from test import counting_valleys_test

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(counting_valleys_test)
    unittest.TextTestRunner(verbosity=2).run(suite)
