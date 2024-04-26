class Calculator:
    def add(self, a, b):
        
        """Adds two numbers and returns the result."""
        return a + b

    def subtract(self, a, b):
        """Subtracts the second number from the first and returns the result."""
        return a - b

    def multiply(self, a, b):
        """Multiplies two numbers and returns the result."""
        return a * b

    def divide(self, a, b):
        """Divides the first number by the second and returns the result.
        
        Raises:
            ZeroDivisionError: If the second number is zero.
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

# Create an instance of Calculator
calc = Calculator()   

# Example of adding two numbers, 7 and 3
result = calc.subtract(2.45, 44)
print(result)