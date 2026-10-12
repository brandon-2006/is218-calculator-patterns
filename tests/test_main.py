
import runpy


def test_main_entry_point(monkeypatch):
    called = []
    monkeypatch.setattr("calculator.cli.main", lambda: called.append(True))

    runpy.run_module("calculator.__main__", run_name="__main__")

    assert called == [True]
