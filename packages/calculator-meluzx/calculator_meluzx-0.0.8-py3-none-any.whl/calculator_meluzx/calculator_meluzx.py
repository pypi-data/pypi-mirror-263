class Calculator:
    """
    Calculator class contains methods for addition, subtraction,
    multiplication, division and root function of Calculator's memory value
    and a variable, that is defined by user.

    Calculator accepts float and int values. In other cases, returns TypeError.
    """

    def __init__(self, print_values=False, memory=0.00):
        """
        Initialization of print_values. Default value is False, meaning the
        answers of called method is not going to be printed. Changing it to
        True will print answer everytime a method is called.
        """
        self.print_values = print_values
        self.memory = memory

    def __repr__(self):
        return f'Memory value: {self.memory:.2f}'

    def _calculate(self, operation, variable):
        """Common method for calculations."""
        try:
            self.memory = round(operation(self.memory, variable), 2)
            if self.print_values:
                print(repr(self))
            return self.memory
        except TypeError:
            return "Input must be a float or an integer."

    def add(self, variable):
        """Takes variable, returns addition to memory value."""
        return self._calculate((lambda x, y: x + y), variable)

    def subtract(self, variable):
        """Takes variable, returns subtraction from memory value."""
        return self._calculate((lambda x, y: x - y), variable)

    def multiply(self, variable):
        """Takes variable, returns multiplication with memory value."""
        return self._calculate((lambda x, y: x * y), variable)

    def divide(self, variable):
        """
        Takes variable, returns division of memory value.

        Returns ValueError if variable is 0.
        """
        try:
            return self._calculate((lambda x, y: x / y), variable)
        except ZeroDivisionError:
            return "Division by 0 not possible."

    def root(self, variable):
        """
        Takes variable, returns variable-th root of memory value.

        Returns ValueError if variable is 0.
        """
        if self.memory >= 0:
            try:
                return self._calculate((lambda x, y: x ** (1 / y)), variable)
            except ZeroDivisionError:
                return "0th root not possible."
        else:
            return "Answer is an imaginary number."

    def reset(self):
        """
        Takes no arguments and sets memory value to 0.
        """
        self.memory = 0.00
        if self.print_values:
            print(repr(self))
        return self.memory

