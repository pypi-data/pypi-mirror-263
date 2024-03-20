# Calculator Package

This package provides a simple calculator class. The fuctions available in calculator:
Addition / Subtraction.
Multiplication / Division.
Take (n) root of a number.


## Installation

You can install the package via pip:

```bash
pip install calculator-package-foxylex
```

## Usage

```python
from calculator.calculator import Calculator

# Create a new calculator instance
calc = Calculator()

# Perform arithmetic operations
calc.add(5)
print("Addition result:", calc.memory)  # Output: 5

calc.subtract(3)
print("Subtraction result:", calc.memory)  # Output: 2

calc.multiply(4)
print("Multiplication result:", calc.memory)  # Output: 8

calc.divide(2)
print("Division result:", calc.memory)  # Output: 4.0

calc.take_root(2)
print("Square root result:", calc.memory)  # Output: 2.0

# Reset the memory
calc.reset_memory()
print("Memory after reset:", calc.memory)  # Output: 0
```

## Operations

The Calculator Package supports the following operations:

Addition
Subtraction
Multiplication
Division
Taking the nth root

## Unit Tests

Unit tests for the Calculator Package are located in the tests/ directory. These tests ensure that each operation functions correctly and that error handling is implemented where necessary. To run the unit tests, use the following command:

```bash
python -m unittest tests.test_calculator
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.