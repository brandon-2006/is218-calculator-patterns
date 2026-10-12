class Operations:
    @staticmethod
    def add(a: float, b: float) -> float:
        # Adds two numbers
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        # Subtracts the second number from the first
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        # Multiplies two numbers
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        # Divides the first number by the second
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

