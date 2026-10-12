
import pytest

from calculator.calculation import ArithmeticCalculation
from calculator.commands import CalculateCommand, HistoryCommand, calculate
from calculator.operations import Operations


def test_calculate_command_records_success():
    history = []
    calculation = ArithmeticCalculation.create(5, 3, Operations.add)
    command = CalculateCommand(calculation, history, "add 5 3")

    assert command.execute() == 8
    assert history == ["add 5 3 = 8"]


def test_failed_calculation_is_not_recorded():
    history = []
    calculation = ArithmeticCalculation.create(5, 0, Operations.divide)
    command = CalculateCommand(calculation, history, "divide 5 0")

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        command.execute()

    assert history == []


def test_history_command_returns_copy():
    history = ["add 5 3 = 8"]
    command = HistoryCommand(history)

    result = command.execute()
    assert result == ["add 5 3 = 8"]

    result.append("fake entry")
    assert history == ["add 5 3 = 8"]


def test_empty_history():
    command = HistoryCommand([])
    assert command.execute() == []


def test_calculate_add():
    assert calculate("add", "5", "3") == 8.0


def test_calculate_subtract():
    assert calculate("subtract", "-2", "5") == -7.0


def test_calculate_multiply():
    assert calculate("multiply", "2.5", "4") == 10.0


def test_calculate_divide():
    assert calculate("divide", "6", "3") == 2.0


def test_calculate_unknown_command():
    with pytest.raises(ValueError, match="Unknown command"):
        calculate("power", "5", "3")


def test_calculate_invalid_first_number():
    with pytest.raises(ValueError, match="Invalid number"):
        calculate("add", "abc", "3")


def test_calculate_invalid_second_number():
    with pytest.raises(ValueError, match="Invalid number"):
        calculate("add", "5", "xyz")
