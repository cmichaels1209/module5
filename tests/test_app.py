import sys
import pytest

class App:
    """This class represents the main application that runs the REPL loop."""
    def start(self, test_mode=False):
        """Start the REPL loop"""
        while True:
            command = input(">>> ").strip()
            if command == "exit":
                print("Exiting...")
                sys.exit(0)  # Use 0 for clean exit
            elif test_mode:
                break  # Prevent infinite loop during tests
            else:
                print(f"No such command: {command}")

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as excinfo:
        app.start(test_mode=True)  # Prevent infinite loop

    # Check that the exit was graceful with the correct exit code
    assert excinfo.value.code == 0

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()

    with pytest.raises(SystemExit):
        app.start()

    # Verify that the unknown command was handled as expected
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out
