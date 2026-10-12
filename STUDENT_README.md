# My calculator submission

Replace these prompts with your own short explanations.

## Setup, run, and test

python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt

python -m calculator

python -m pytest

python -m pytest --cov=calculator --cov-report=term-missing --cov-fail-under=100

## Example conversation

> add 5 3
8.0
> multiply 2.5 4
10.0
> history
add 5 3 = 8.0
multiply 2.5 4 = 10.0
> divide 5 0
Cannot divide by zero
> history
add 5 3 = 8.0
multiply 2.5 4 = 10.0
> exit

## Static, class, and instance methods

A static method does not need an object or class state.

The class method ArithmeticCalculation.create(a, b, operation) creates and returns an ArithmeticCalculation object 

The instance method execute() uses the values stored in a calculation object and returns the result
## Factory, Command, and Strategy

The user enters add 5 3, the CLI reads and splits the input into a command name and two operands. It checks that the command exists and converts the operands to numbers.

Operations.add passes that function to ArithmeticCalculation.create(5, 3, Operations.add), which creates the calculation object.

CLI then creates a CalculateCommand with the calculation and shared history list. Calling execute() runs the calculation, records the successful result

## OOP

Encapsulation: Calculation stores its operands and operation in instance attributes. CalculateCommand keeps the calculation, history list, and label together in one object.

Abstraction: Calculation defines the abstract execute() method, specifying what a concrete calculation must provide without defining its arithmetic implementation.

Inheritance: ArithmeticCalculation inherits from Calculation and implements execute().

Polymorphism: Different operation functions can be passed to the same calculation class. Calling execute() performs the selected operation.

Composition: CalculateCommand contains a calculation object and a reference to the shared history list. It uses these objects to perform its job.

## SOLID

 Operations handles arithmetic, Calculation represents calculations, command classes handle actions and history, and cli.py handles user input and output.

 A new operation can be added as another static method in Operations and registered in the operation dictionary. The calculation execution method does not need to change.

## Tests and GitHub Actions

https://github.com/brandon-2006/is218-calculator-patterns/actions/runs/38211342699
## Coverage exclusions

The starter excludes the abstract Calculation.execute() placeholder because it declares the required method but contains no implementation to execute. The concrete ArithmeticCalculation.execute() method is tested.
