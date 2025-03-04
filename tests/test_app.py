import pytest
from app import App


def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')

    app = App()

    with pytest.raises(SystemExit) as e:
        app.start()

    # Check if the exit message is correct
    assert str(e.value) == "Exiting...", "Expected 'Exiting...' message"

    # Capture the standard output
    out, _ = capfd.readouterr()
    assert "Type 'exit' to exit." in out, "Expected startup message in output"


def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit) as e:
        app.start()

    # Capture the standard output
    out, _ = capfd.readouterr()
    assert "No such command: unknown_command" in out, "Expected unknown command message"
    assert str(e.value) == "Exiting...", "Expected 'Exiting...' message"
