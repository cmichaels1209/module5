import sys
import pkgutil
import importlib
from app.commands import CommandHandler, Command

class App:
    def __init__(self):  # Constructor
        self.command_handler = CommandHandler()

    def load_plugins(self):
        """Dynamically load all plugins in the app.plugins directory."""
        plugins_package = "app.plugins"
        try:
            package = importlib.import_module(plugins_package)
            for _, plugin_name, is_pkg in pkgutil.iter_modules(package.__path__, f"{plugins_package}."):
                if not is_pkg:  # Ignore non-package modules
                    plugin_module = importlib.import_module(plugin_name)
                    for item_name in dir(plugin_module):
                        item = getattr(plugin_module, item_name)
                        if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                            self.command_handler.register_command(plugin_name.split(".")[-1], item())
        except ModuleNotFoundError as e:
            print(f"Warning: Could not load plugins. {e}")

    def start(self):
        """Start the REPL loop."""
        self.load_plugins()
        print("Type 'exit' to exit or 'menu' to see available commands.")
        while True:  # REPL Read, Evaluate, Print, Loop
            user_input = input(">>> ").strip().lower()
            if user_input == "exit":
                print("Exiting...")
                sys.exit(0)
            elif user_input == "menu":
                print("Available Commands:")
                for cmd in self.command_handler.commands.keys():
                    print(f" - {cmd}")
            else:
                self.command_handler.execute_command(user_input)

if __name__ == "__main__":
    app = App()
    app.start()
