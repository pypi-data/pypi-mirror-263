class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations
    and manipulation of memory.

    Attributes:
        memory (float): The current value stored in the calculator's memory.
    """

    def __init__(self) -> None:
        """
        Initializes the Calculator with memory set to 0.
        """
        self.memory: float = 0

    def _check_number_type(self, num: float) -> None:
        """
        Checks if the provided argument is a valid number.

        Args:
            num (float): The number to be checked.

        Raises:
            TypeError: If the argument is not a valid number.
        """
        if not isinstance(num, (int, float)):
            raise TypeError("Argument must be a number")

    def add(self, num: float) -> None:
        """
        Adds a number to the memory.

        Args:
            num (float): The number to be added to the memory.
        """
        self._check_number_type(num)
        self.memory += num

    def subtract(self, num: float) -> None:
        """
        Subtracts a number from the memory.

        Args:
            num (float): The number to be subtracted from the memory.
        """
        self._check_number_type(num)
        self.memory -= num

    def multiply(self, num: float) -> None:
        """
        Multiplies the memory by a given number.

        Args:
            num (float): The number to multiply the memory by.
        """
        self._check_number_type(num)
        self.memory *= num

    def divide(self, num: float) -> None:
        """
        Divides the memory by a given number.

        Args:
            num (float): The number to divide the memory by.

        Raises:
            ValueError: If num is 0, as division by zero is not allowed.
            TypeError: If num is not a valid number.
        """
        self._check_number_type(num)
        if num == 0:
            raise ValueError("Cannot divide by zero")
        self.memory /= num

    def take_root(self, n: int) -> None:
        """
        Takes the n-th root of the memory.

        Args:
         n (int): The root to be taken.

        Raises:
            ValueError: If the memory is negative,
                        as real roots of negative numbers are not defined.
            TypeError: If n is not an integer.
        """
        if not isinstance(n, int):
            raise TypeError("Root must be an integer")
        if self.memory < 0:
           raise ValueError("Cannot take root of a negative number")
        if self.memory == 0 and n < 0:
            raise ValueError("Cannot take 0th root")
        self.memory **= (1 / n)

    def reset_memory(self) -> None:
        """
        Resets the memory of the calculator to 0.
        """
        self.memory = 0
