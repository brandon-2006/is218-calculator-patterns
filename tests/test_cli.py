
from calculator.cli import main


def run_cli(monkeypatch, capsys, commands):
    answers = iter(commands)
    monkeypatch.setattr("builtins.input", lambda prompt="": next(answers))
    main()
    return capsys.readouterr().out


def test_cli_add_then_exit(monkeypatch, capsys):
    output = run_cli(monkeypatch, capsys, ["add 5 3", "exit"])
    assert "8.0" in output


def test_cli_history(monkeypatch, capsys):
    output = run_cli(
        monkeypatch,
        capsys,
        ["add 5 3", "history", "exit"],
    )
    assert "add 5 3 = 8.0" in output


def test_cli_unknown_command(monkeypatch, capsys):
    output = run_cli(monkeypatch, capsys, ["power 5 3", "exit"])
    assert "Unknown command" in output


def test_cli_wrong_operand_count(monkeypatch, capsys):
    output = run_cli(monkeypatch, capsys, ["add 5", "exit"])
    assert "exactly two numbers" in output


def test_cli_invalid_number(monkeypatch, capsys):
    output = run_cli(monkeypatch, capsys, ["add abc 3", "exit"])
    assert "Invalid number" in output


def test_cli_divide_by_zero_and_continue(monkeypatch, capsys):
    output = run_cli(
        monkeypatch,
        capsys,
        ["divide 5 0", "add 2 3", "history", "exit"],
    )
    assert "Cannot divide by zero" in output
    assert "5.0" in output
    assert "divide 5 0" not in output


def test_cli_empty_history(monkeypatch, capsys):
    output = run_cli(monkeypatch, capsys, ["history", "exit"])
    assert "History is empty" in output


def test_cli_blank_line(monkeypatch, capsys):
    output = run_cli(monkeypatch, capsys, ["", "add 2 3", "exit"])
    assert "5.0" in output


def test_cli_eof(monkeypatch, capsys):
    def end_of_input(prompt=""):
        raise EOFError

    monkeypatch.setattr("builtins.input", end_of_input)
    main()

    # EOF should end the CLI without an uncaught exception.
    assert capsys.readouterr().out == ""
