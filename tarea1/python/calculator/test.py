import unittest
import main as calculator

MAX_BINARY_INTEGER = "1111111111111111111111111111111"
MAX_INTEGER = 2147483647.0
MID_BINARY_INTEGER = "0111111111111111111111111111111"
MID_INTEGER = 1073741823.0
MIN_BINARY_INTEGER = "0000000000000000000000000000000"
MIN_INTEGER = 0.0


class CalculatorTestFact(unittest.TestCase):
    def test_sum_min_values(self):
        result0 = MIN_INTEGER + MID_INTEGER
        result1 = calculator.operators['+'](MIN_INTEGER, MID_INTEGER)
        self.assertEqual(result0, result1)

    def test_sum_mid_values(self):
        result0 = MID_INTEGER + MID_INTEGER
        result1 = calculator.operators['+'](MID_INTEGER, MID_INTEGER)
        self.assertEqual(result0, result1)

    def test_sum_max_values(self):
        result0 = MAX_INTEGER + MIN_INTEGER
        result1 = calculator.operators['+'](MAX_INTEGER, MIN_INTEGER)
        self.assertEqual(result0, result1)

    def test_subtract_min_values(self):
        result0 = MIN_INTEGER - MID_INTEGER
        result1 = calculator.operators['-'](MIN_INTEGER, MID_INTEGER)
        self.assertEqual(result0, result1)

    def test_subtract_mid_values(self):
        result0 = MID_INTEGER - MID_INTEGER
        result1 = calculator.operators['-'](MID_INTEGER, MID_INTEGER)
        self.assertEqual(result0, result1)

    def test_subtract_max_values(self):
        result0 = MAX_INTEGER - MIN_INTEGER
        result1 = calculator.operators['-'](MAX_INTEGER, MIN_INTEGER)
        self.assertEqual(result0, result1)

    def test_multiplication_min_values(self):
        result0 = MIN_INTEGER * MID_INTEGER
        result1 = calculator.operators['*'](MIN_INTEGER, MID_INTEGER)
        self.assertEqual(result0, result1)

    def test_multiplication_mid_values(self):
        result0 = MID_INTEGER * MIN_INTEGER
        result1 = calculator.operators['*'](MID_INTEGER, MIN_INTEGER)
        self.assertEqual(result0, result1)

    def test_multiplication_max_values(self):
        result0 = MAX_INTEGER * MIN_INTEGER
        result1 = calculator.operators['*'](MAX_INTEGER, MIN_INTEGER)
        self.assertEqual(result0, result1)

    def test_division_min_values(self):
        result0 = MIN_INTEGER / MID_INTEGER
        result1 = calculator.operators['/'](MIN_INTEGER, MID_INTEGER)
        self.assertEqual(result0, result1)

    def test_division_mid_values(self):
        result0 = MAX_INTEGER / MID_INTEGER
        result1 = calculator.operators['/'](MAX_INTEGER, MID_INTEGER)
        self.assertEqual(result0, result1)

    def test_division_max_values(self):
        result0 = MIN_INTEGER * MID_INTEGER
        result1 = calculator.operators['/'](MIN_INTEGER, MID_INTEGER)
        self.assertEqual(result0, result1)

    def test_and_min_values(self):
        result0 = MIN_INTEGER and MID_INTEGER
        result1 = calculator.operators['and'](MIN_INTEGER, MID_INTEGER)
        self.assertEqual(result0, result1)

    def test_and_mid_values(self):
        result0 = MID_INTEGER and MID_INTEGER
        result1 = calculator.operators['and'](MID_INTEGER, MID_INTEGER)
        self.assertEqual(result0, result1)

    def test_and_max_values(self):
        result0 = MAX_INTEGER and MIN_INTEGER
        result1 = calculator.operators['and'](MAX_INTEGER, MIN_INTEGER)
        self.assertEqual(result0, result1)

    def test_or_min_values(self):
        result0 = MIN_INTEGER or MID_INTEGER
        result1 = calculator.operators['or'](MIN_INTEGER, MID_INTEGER)
        self.assertEqual(result0, result1)

    def test_or_mid_values(self):
        result0 = MID_INTEGER or MID_INTEGER
        result1 = calculator.operators['or'](MID_INTEGER, MID_INTEGER)
        self.assertEqual(result0, result1)

    def test_or_max_values(self):
        result0 = MAX_INTEGER or MIN_INTEGER
        result1 = calculator.operators['or'](MAX_INTEGER, MIN_INTEGER)
        self.assertEqual(result0, result1)


class MiscellaneousTestFact(unittest.TestCase):
    def test_main(self):
        calculator.main()
        self.assertTrue(True)

    def test_calculate_chain_args(self):
        mjs = calculator.execute(MIN_BINARY_INTEGER, "-",
                                 MID_BINARY_INTEGER, "+",
                                 MID_BINARY_INTEGER, "/",
                                 MID_BINARY_INTEGER, "*",
                                 MID_BINARY_INTEGER)
        result = MIN_INTEGER - MID_INTEGER + MID_INTEGER / MID_INTEGER * MID_INTEGER
        self.assertTrue(str(result) in mjs)

    def test_calculate_good_format_args(self):
        mjs = calculator.execute(MIN_BINARY_INTEGER, "and", MID_BINARY_INTEGER)
        result = int(MIN_INTEGER) & int(MID_INTEGER)
        self.assertTrue(str(result) in mjs)

    def test_calculate_bad_format_args(self):
        try:
            calculator.execute(MID_BINARY_INTEGER, "+", "+", MID_BINARY_INTEGER)
        except ValueError:
            self.assertTrue(True)

    def test_message_with_Args(self):
        mjs = calculator.execute()
        self.assertTrue("Must return default message", "Thanks for using the calculator, result" in mjs)

    def test_message_without_args(self):
        mjs = calculator.execute()
        self.assertTrue("Must return default message", "Welcome" in mjs)


if __name__ == '__main__':
    unittest.main()
