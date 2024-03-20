class Calculator:
    """
    Calculator class contains methods for addition, subtraction, multiplication,
    division and root function of Calculator's memory value and a variable,
    that is defined by user.
    Following code line sets initial Calculator's memory value to 0.
    """
    memory = 0.0

    def add(self, variable):
        """Definition of a method that performs addition"""
        self.memory = round(self.memory + variable, 2)
        return float("%.2f" % self.memory)

    def subtract(self, variable):
        """Definition of a method that performs subtraction"""
        self.memory = round(self.memory - variable, 2)
        return float("%.2f" % self.memory)

    def multiply(self, variable):
        """Definition of a method that performs multiplication"""
        self.memory = round(self.memory * variable, 2)
        return float("%.2f" % self.memory)

    def divide(self, variable):
        """
        Definition of a method that performs division.
        Restrictions:
        1. input cannot be 0. In that case, method returns 'Invalid'.
        """
        if variable != 0.0:
            self.memory = round(self.memory / variable, 2)
            return float("%.2f" % self.memory)
        else:
            return "Division by 0 not possible"

    def root(self, variable):
        """
        Definition of a method that finds n-th root of a number.
        Restrictions:
        1. calculator's memory cannot be less than 0. In that case, method
        returns 'Answer is imaginary number';
        2. input cannot be 0. In case it is, method returns 'Invalid'.
        """
        if self.memory >= 0:
            if variable != 0:
                self.memory = round(self.memory ** (1 / variable), 2)
                return float("%.2f" % self.memory)
            else:
                return "Invalid"
        else:
            return "Answer is an imaginary number"

    def reset(self):
        """
        Definition of a method that sets calculator's memory to initial value
        """
        self.memory = Calculator.memory
        return float("%.2f" % self.memory)

