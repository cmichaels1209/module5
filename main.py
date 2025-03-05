from app import App

def main():
    """Main entry point for the application."""
    app = App()  # Create an instance of the App
    app.start()  # Call start() on the instance, not the class

if __name__ == "__main__":
    main()
