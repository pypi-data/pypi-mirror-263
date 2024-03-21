from src.calculator_meluzx.calculator_meluzx import Calculator
import unittest

cal = Calculator()


class TestCalculations(unittest.TestCase):
    """Class for testing Calculator's module. Checks if reset fu nction is
    working, runs cases with positive and negative numbers as well as zeros.
    Check special root cases, when calculator's memory is a negative value.
    Also checks if the TypeError is raised in case user defined variable is a
    string"""
    def test_reset(self):
        """Tests if reset method works"""
        assert cal.reset() == 0, "Reset does not work"

    def test_positive(self):
        """Tests cases with positive numbers"""
        cal.reset()
        assert cal.add(26) == 26
        assert cal.subtract(6) == 20
        assert cal.multiply(2) == 40
        assert cal.divide(4) == 10
        assert cal.root(3) == 2.15

    def test_negative(self):
        """Tests cases with negative numbers"""
        cal.reset()
        assert cal.add(-1) == -1
        assert cal.subtract(-5) == 4
        assert cal.multiply(-3) == -12
        assert cal.divide(-3) == 4
        assert cal.root(-2) == 0.5

    def test_zeros(self):
        """Tests cases with zeros"""
        cal.reset()
        assert cal.add(0) == 0
        assert cal.subtract(0) == 0
        assert cal.multiply(0) == 0
        assert cal.divide(0) == "Division by 0 not possible."
        assert cal.root(0) == "0th root not possible."

    def test_root_with_negative_memory_value(self):
        """Tests cases with negative memory value"""
        cal.reset()
        cal.add(-5)
        assert cal.root(2) == "Answer is an imaginary number."

    def test_str(self):
        """Tests cases with string variables"""
        cal.reset()
        assert cal.add("a") == "Input must be a float or an integer."
        assert cal.subtract("10") == "Input must be a float or an integer."
        assert cal.multiply("a") == "Input must be a float or an integer."
        assert cal.divide("a") == "Input must be a float or an integer."
        assert cal.root("1") == "Input must be a float or an integer."


if __name__ == '__main__':
    unittest.main()

"""
def main():
    test_positive()
    test_negative()
    test_zeros()
    test_str()


def test_positive():
    assert cal.reset() == 0
    assert cal.add(26) == 26
    assert cal.subtract(6) == 20
    assert cal.multiply(2) == 40
    assert cal.divide(4) == 10
    assert cal.root(3) == 2.15


def test_negative():
    assert cal.reset() == 0
    assert cal.add(-10) == -10
    assert cal.subtract(-5) == -5
    assert cal.multiply(-3) == 15
    assert cal.divide(-5) == -3
    assert cal.root(-2) == "Answer is imaginary number"


def test_zeros():
    assert cal.reset() == 0
    assert cal.add(0) == 0
    assert cal.subtract(0) == 0
    assert cal.multiply(0) == 0
    assert cal.divide(0) == "Division by 0 not possible"
    assert cal.root(0) == "Invalid"


def test_str():
    with pytest.raises(TypeError):
        cal.add("a")
        cal.subtract("10")
        cal.multiply("a")
        cal.divide("a")
        cal.root("1")


if __name__ == "__main__":
    main()
"""
