from calculator.calculation import Calculation
from calculator.operations import Operations
from calculator.calculation import ArithmeticCalculation

operations = {
    "add": Operations.add,
    "subtract": Operations.subtract,
    "multiply": Operations.multiply,
    "divide": Operations.divide,
}


def calculate(command_name, first, second):
    if command_name not in operations:
        raise ValueError(f"Unknown command: {command_name}")

    try:
        a = float(first)
        b = float(second)
    except ValueError:
        raise ValueError("Invalid number") from None

    operation = operations[command_name]
    calculation = ArithmeticCalculation.create(a, b, operation)
    return calculation.execute()


class CalculateCommand:
    def __init__(
        self,
        calculation: Calculation,
        history: list[str],
        label: str = "calculation",
    ):
        # The command receives its calculation and shared history.
        self.calculation = calculation
        self.history = history
        self.label = label

    def execute(self) -> float:
        # Run the calculation first. If it fails, history stays unchanged.
        result = self.calculation.execute()

        # Record only successful calculations.
        self.history.append(f"{self.label} = {result}")

        return result


class HistoryCommand:
    def __init__(self, history: list[str]):
        self.history = history

    def execute(self) -> list[str]:
        # Return a copy so callers cannot change stored history.
        return self.history.copy()

