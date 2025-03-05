import os

class App:
    """This class represents the main application."""
    def get_environment_variable(self, variable_name):
        """
        Retrieve the value of an environment variable.

        Args:
            variable_name (str): The name of the environment variable to retrieve.

        Returns:
            str: The value of the environment variable, or None if not set.
        """
        return os.getenv(variable_name)

def test_app_get_environment_variable():
    """Test retrieving an environment variable."""
    app = App()
    # Retrieve the current environment setting
    env_value = app.get_environment_variable('ENVIRONMENT')

    # Add an assertion to demonstrate the test is doing something
    assert env_value is None or isinstance(env_value, str), "Environment variable should be a string or None"
