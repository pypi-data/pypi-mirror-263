from typing import Optional

class Calculator:
    """ A class, which has a variable to store memory (_memory)
    and 6 methods (add, subtract, multiply, divide, root, reset).
    The first 5 methods provide arithmetic operations and the
    last method resets Calculator's memory variable """

    _memory: float = 0  # Class variable to store memory

    def add(x: float, y: Optional[float]=None) -> float:
        """Addition - returns float stored in _memory + x
         or, if optional argument y is provided, returns x + y"""
        if y is not None:
            Calculator._memory = x + y
            return Calculator._memory
        else:
            Calculator._memory += x
            return Calculator._memory

    def subtract(x: float, y: Optional[float]=None) -> float:
        """Subtraction - returns float stored in _memory - x
         or, if optional argument y is provided, returns x - y"""
        if y is not None:
            Calculator._memory = x - y
            return Calculator._memory
        else:
            Calculator._memory -= x
            return Calculator._memory

    def multiply(x: float, y: Optional[float]=None) -> float:
        """Multiplication - returns float stored in _memory * x
         or, if optional argument y is provided, returns x * y"""
        if y is not None:
            Calculator._memory = x * y
            return Calculator._memory
        else:
            Calculator._memory *= x
            return Calculator._memory

    def divide(x: float, y: Optional[float]=None) -> float:
        """Division - returns float stored in _memory / x
         or, if optional argument y is provided, returns x / y"""

        if y is not None:
            Calculator._memory = x / y
        else:
            Calculator._memory /= x
        return Calculator._memory

    def root(x: float, y: Optional[float]=None) -> float:
        """Root - returns x-th root of float stored in _memory
         or, if optional argument y is provided, returns y-th root of x"""
        if y == 0:
            raise ValueError("Root cannot be zero")
        elif y is None and x == 0:
            raise ValueError("Root cannot be zero")
        
        if y is not None:
            if x < 0:
                raise ValueError("Cannot get a root of a negative number")
            Calculator._memory = x ** (1 / y)
        else:
            if Calculator._memory < 0:
                raise ValueError("Cannot get a root of a negative number")
            Calculator._memory **= (1 / x)
        return Calculator._memory
        
    def reset() -> None:
        """Sets class variable _memory to 0"""
        Calculator._memory = 0
