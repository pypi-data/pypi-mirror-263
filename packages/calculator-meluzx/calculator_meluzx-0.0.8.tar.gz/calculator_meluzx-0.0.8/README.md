# Calculator

Calculator is a Python package for performing addition, subtraction, multiplication, 
division and n-th root functions on a number stored in calculator's memory. Everytime a 
function is performed, calculator's memory is updated.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to this calculator as calculator-meluzx==0.0.7.
```bash
pip install calculator-meluzx==0.0.8
```
## Usage

To import this package, use the following code.
```python
from calculator_meluzx.calculator_meluzx import Calculator

# activates calculator with initial memory's value 
calculator = Calculator()
```
The initial value stored in calculator's memory is 0. All functions are performed with 
latest value in calculator's memory and a number, defined in brackets when calling a 
method. The following code describes a case, in which some prior functions have been 
performed and latest value in calculator's memory is 2.
```python
# performs 2 + 3, returns 5
calculator.add(3)

# performs 5 - 4, returns 1
calculator.subtract(4)

# performs 1 * 8, returns 8
calculator.multiply(8)

# performs 8 / 2, returns 4
calculator.divide(2)

# performs 4 ** 2, returns 2
calculator.root(2)
```
Calculator also has reset function, which sets calculator's memory value to 0.
```python
# returns 0
calculator.reset()
```

## Requirements
This package is introduced in Python3.12 and works with python versions >= 3.6. For 
installation you need to have pip module in your environment.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss 
what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)