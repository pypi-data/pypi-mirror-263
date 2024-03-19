# Calculator

Calculator is a Python library that provides basic arithmetic operations.

## Installation

You can install Calculator using pip:

```bash
python -m pip install calculatormp
```

## Usage

Calculator provides add, subtract, multiply, divide, root and reset static methods of class Calculator. Each method (apart from reset) can take up to 2 arguments. If 1 argument is given, variable _memory (by default set to 0) is updated based on the chosen method, and its value is returned. If 2 arguments are given, variable _memory is set and returned based on the operation provided by the chosen method and 2 arguments. Giving 2 arguments disregards previous history of operations and automatically sets _memory to a new value. _memory can be manually set to 0 using reset() method.

```python
from calculatormp.calculator import Calculator

# Addition - returns float stored in _memory + x
Calculator.add(5) # returns 5
# If optional argument y is provided, returns x + y
Calculator.add(5, 5) # returns 10


# Subtraction - returns float stored in _memory - x
Calculator.substract(5) # returns -5
# if optional argument y is provided, returns x - y
Calculator.substract(10, 5) # returns 5


# Multiplication - returns float stored in _memory * x
Calculator.add(5) # _memory = 5
Calculator.multiply(5) # returns 25
# if optional argument y is provided, returns x * y
Calculator.multiply(2, 10) # returns 20


# Division - returns float stored in _memory / x
Calculator.add(5) # _memory = 5
Calculator.divide(5) # returns 1
# if optional argument y is provided, returns x / y
Calculator.divide(10, 2) # returns 5


# Root - returns x-th root of float stored in _memory
Calculator.add(16) # _memory = 16
Calculator.root(2) # returns 4
# if optional argument y is provided, returns y-th root of x
Calculator.root(16, 2) # returns 4

# Reset - sets variable _memory to 0
Calculator.add(50) # returns 50
Calculator.add(5) # returns 55
Calculator.reset()
Calculator.add(1) # returns 1
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)