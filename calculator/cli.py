
from calculator.operations import Operations
from calculator.calculation import ArithmeticCalculation
from calculator.commands import CalculateCommand, HistoryCommand


def main():
    operations = {
        "add": Operations.add,
        "subtract": Operations.subtract,
        "multiply": Operations.multiply,
        "divide": Operations.divide,
    }
    history = []

    while True:
        try:
            words = input("> ").split()
        except EOFError:
            break

        # Ignore blank lines and handle exit/history commands.
        if not words:
            continue

        command_name = words[0].lower()

        if command_name == "exit":
            break

        if command_name == "history":
            entries = HistoryCommand(history).execute()
            if entries:
                for entry in entries:
                    print(entry)
            else:
                print("History is empty.")
            continue

        # Check the command name and number of operands.
        if command_name not in operations:
            print(f"Unknown command: {command_name}")
            continue

        if len(words) != 3:
            print("Please provide exactly two numbers.")
            continue

        # Convert operands and handle invalid numbers.
        try:
            a = float(words[1])
            b = float(words[2])
        except ValueError:
            print("Invalid number. Please enter valid numbers.")
            continue

        # Read input -> choose strategy -> create calculation
        # -> create and execute command -> print the answer.
        operation = operations[command_name]
        calculation = ArithmeticCalculation.create(a, b, operation)
        command = CalculateCommand(
            calculation,
            history,
            f"{command_name} {words[1]} {words[2]}",
        )

        try:
            result = command.execute()
            print(result)
        except ValueError as error:
            print(error)
