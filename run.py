# #!/usr/bin/env python3
# """
# AgroUSSD Launcher Script
# Simple launcher for the AgroUSSD application
# """

# import sys
# import os

# # Add the src directory to the Python path
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# # Import and run the main application
# from main import main

# if __name__ == "__main__":
#     main()


from src.interfaces.session_manager import SessionManager

def main():
    session = SessionManager()
    while True:
        current_menu = session.get_current_menu()
        current_menu.display()
        choice = input("Enter choice: ")
        current_menu.handle_input(choice)

if __name__ == "__main__":
    main()
