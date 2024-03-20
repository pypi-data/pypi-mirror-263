import unittest
from calculator.calculator import Calculator


class TestCalculator(unittest.TestCase):
    """
    A class containing unit tests for the Calculator class.

    These tests cover positive, negative scenarios, and error cases
    to ensure the correctness and robustness of the Calculator class.

    Methods:
        setUp(): A setup method that initializes a Calculator instance.
        test_add_positive(): Tests addition with a positive number.
        test_add_negative(): Tests addition with a negative number.
        test_subtract_positive(): Tests subtraction with a positive number.
        test_subtract_negative(): Tests subtraction with a negative number.
        test_multiply_positive(): Tests multiplication with a positive number.
        test_multiply_negative(): Tests multiplication with a negative number.
        test_divide_positive(): Tests division with a positive divisor.
        test_divide_by_zero(): Tests division by zero.
        test_take_root_positive(): Tests taking a positive root.
        test_take_root_negative(): Tests taking a root of a negative number.
        test_take_root_non_integer(): Tests taking a non-integer root.
        test_reset_memory(): Tests resetting the memory of the calculator.
        test_invalid_argument_type(): Tests passing an invalid argument type.
        test_invalid_api_usage(): Tests calling arithmetic methods with invalid argument types.
    """

    def setUp(self):
        """
        Initializes a Calculator instance before each test method.
        """
        self.calc = Calculator()

    # Positive scenario tests
    def test_add_positive(self):
        """
        Tests addition with a positive number.
        """
        self.calc.add(5)
        self.assertEqual(self.calc.memory, 5)

    def test_subtract_positive(self):
        """
        Tests subtraction with a positive number.
        """
        self.calc.subtract(3)
        self.assertEqual(self.calc.memory, -3)

    def test_multiply_positive(self):
        """
        Tests multiplication with a positive number.
        """
        self.calc.memory = 2
        self.calc.multiply(3)
        self.assertEqual(self.calc.memory, 6)

    def test_divide_positive(self):
        """
        Tests division with a positive divisor.
        """
        self.calc.memory = 10
        self.calc.divide(2)
        self.assertEqual(self.calc.memory, 5)

    def test_take_root_positive(self):
        """
        Tests taking a positive root.
        """
        self.calc.memory = 8
        self.calc.take_root(3)
        self.assertEqual(self.calc.memory, 2)

    def test_reset_memory(self):
        """
        Tests resetting the memory of the calculator.
        """
        self.calc.memory = 10
        self.calc.reset_memory()
        self.assertEqual(self.calc.memory, 0)

    # Negative scenario tests
    def test_add_negative(self):
        """
        Tests addition with a negative number.
        """
        self.calc.add(-3)
        self.assertEqual(self.calc.memory, -3)

    def test_subtract_negative(self):
        """
        Tests subtraction with a negative number.
        """
        self.calc.subtract(-2)
        self.assertEqual(self.calc.memory, 2)

    def test_multiply_negative(self):
        """
        Tests multiplication with a negative number.
        """
        self.calc.memory = -3
        self.calc.multiply(2)
        self.assertEqual(self.calc.memory, -6)

    # Error case tests
    def test_divide_by_zero(self):
        """
        Tests division by zero.
        """
        with self.assertRaises(ValueError):
            self.calc.divide(0)

    def test_take_root_negative(self):
        """
        Tests taking a root of a negative number.
        """
        self.calc.memory = -8
        with self.assertRaises(ValueError):
            self.calc.take_root(3)

    def test_take_root_non_integer(self):
        """
        Tests taking a non-integer root.
        """
        self.calc.memory = 5.5
        with self.assertRaises(TypeError):
            self.calc.take_root(1.5)

    def test_invalid_argument_type(self):
        """
        Tests passing an invalid argument type.
        """
        with self.assertRaises(TypeError):
            self.calc.add("invalid")

    def test_invalid_api_usage(self):
        """
        Tests calling arithmetic methods with invalid argument types.
        """
        with self.assertRaises(TypeError):
            self.calc.add("invalid_argument")

if __name__ == '__main__':
    unittest.main()
