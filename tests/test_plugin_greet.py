from app.commands import Command

class GreetCommand(Command):
    def execute(self):
        """Print a greeting."""
        print("Hello, World!")
