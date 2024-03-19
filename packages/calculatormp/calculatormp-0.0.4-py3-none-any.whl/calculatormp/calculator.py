from typing import Optional

class Calculator:
    _memory: float = 0  # Class variable to store memory

    @staticmethod
    def add(x: float, y: Optional[float]=None) -> float:
        """Addition - returns float stored in _memory + x
         or, if optional argument y is provided, returns x + y"""
        if y is not None:
            Calculator._memory = x + y
            return Calculator._memory
        else:
            Calculator._memory += x
            return Calculator._memory

    @staticmethod
    def subtract(x: float, y: Optional[float]=None) -> float:
        """Subtraction - returns float stored in _memory - x
         or, if optional argument y is provided, returns x - y"""
        if y is not None:
            Calculator._memory = x - y
            return Calculator._memory
        else:
            Calculator._memory -= x
            return Calculator._memory

    @staticmethod
    def multiply(x: float, y: Optional[float]=None) -> float:
        """Multiplication - returns float stored in _memory * x
         or, if optional argument y is provided, returns x * y"""
        if y is not None:
            Calculator._memory = x * y
            return Calculator._memory
        else:
            Calculator._memory *= x
            return Calculator._memory

    @staticmethod
    def divide(x: float, y: Optional[float]=None) -> float:
        """Division - returns float stored in _memory / x
         or, if optional argument y is provided, returns x / y"""
        if y == 0:
            raise ValueError("Cannot divide by zero")
        
        if y is not None:
            Calculator._memory = x / y
        else:
            if x == 0:
                raise ValueError("Cannot divide by zero")
            Calculator._memory /= x
        return Calculator._memory

    @staticmethod
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
        
    @staticmethod
    def reset() -> None:
        """Sets class variable _memory to 0"""
        Calculator._memory = 0