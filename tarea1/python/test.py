import unittest
from main import Calculator

class TestCalculator(unittest.TestCase):
    def test_sample(self):
        cal = Calculator()
        self.assertEqual(cal.helloWorld(), "Hello world!")

if __name__ == '__main__':
    unittest.main()