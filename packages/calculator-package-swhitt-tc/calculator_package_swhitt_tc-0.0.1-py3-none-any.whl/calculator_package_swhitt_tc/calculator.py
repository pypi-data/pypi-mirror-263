class Calculator:
    """A calculator object that performs simple mathematical operations.
    
    Attributes:
        default_num: an integer initialized to 0 upon which mathematical operations are performed.
        add: a function that adds a single integer input to the default number.
        subtract: a function that subtracts a single integer input from the defaul number.
        multiply: a function that multiplies the default number by a single integer input.
        divide: a function that divides the default number by a single integer input.
        nth_root: a function that nth root of the default number, where n is equal to a single integer input.
        reset: a function that resets the default number.
    """
    
    default_num: int = 0
    
    def __init__(self, num1: int = None):
        """Initializes Calculator with a default integer 0."""
        if num1 == None:
            num1 = Calculator.default_num
            print(num1)
        else:
            Calculator.default_num = num1
            print(Calculator.default_num)
        
    def add(self, num2: int) -> int:
        """Compute the sum of two integers."""
        Calculator.default_num += num2
        return Calculator.default_num
    
    def subtract(self, num2: int) -> int:
        """Compute the difference of two integers."""
        Calculator.default_num -= num2
        return Calculator.default_num
    
    def multiply(self, num2: int) -> int:
        """Compute the product of two integers."""
        Calculator.default_num *= num2
        return Calculator.default_num
    
    def divide(self, num2: int) -> int:
        """Compute the quotient of two integers."""
        Calculator.default_num /= num2
        return Calculator.default_num
    
    def nth_root(self, num2: int) -> int:
        """Compute the nth root of an integer."""
        Calculator.default_num = Calculator.default_num ** (1 / num2)
        return Calculator.default_num
    
    def reset(self, num2: int = None):
        """Reset the memory of the calculator program."""
        if num2 == None:
            num2 = 0
            Calculator.default_num = num2
            return Calculator.default_num
        else:
            Calculator.default_num = num2
            return Calculator.default_num
    

    


    

        
