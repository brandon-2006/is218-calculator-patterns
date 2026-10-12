
import pytest

from calculator.calculation import Calculation, ArithmeticCalculation
from calculator.operations import Operations


def test_factory_creates_calculation():
    calculation = ArithmeticCalculation.create(5, 3, Operations.add)

    assert isinstance(calculation, ArithmeticCalculation)
    assert calculation.a == 5
    assert calculation.b == 3
    assert calculation.operation is Operations.add
    assert calculation.execute() == 8


def test_calculation_uses_different_operations():
    subtraction = ArithmeticCalculation.create(5, 3, Operations.subtract)
    multiplication = ArithmeticCalculation.create(5, 3, Operations.multiply)
    division = ArithmeticCalculation.create(6, 3, Operations.divide)

    assert subtraction.execute() == 2
    assert multiplication.execute() == 15
    assert division.execute() == 2


def test_abstract_calculation_cannot_be_created():
    with pytest.raises(TypeError):
        Calculation(5, 3, Operations.add)
