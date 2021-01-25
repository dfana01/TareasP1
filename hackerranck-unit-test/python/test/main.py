import unittest
from test import counting_valleys_test, array_2d_ds_test


def run_suite(module):
    suite = unittest.TestLoader().loadTestsFromModule(module)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    run_suite(counting_valleys_test)
    run_suite(array_2d_ds_test)
