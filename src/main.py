#!/usr/bin/env python3
"""
AgroUSSD - Agricultural Marketplace USSD Simulation
Main application engine that runs the USSD simulation
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from interfaces.session_manager import SessionManager
from interfaces.main_menu import MainMenu

def main():
    """Main application entry point"""
    print("Starting AgroUSSD - Agricultural Marketplace...")
    
    # Initialize session manager
    session_manager = SessionManager()
    
    # Start with main menu
    current_interface = MainMenu(session_manager)
    
    try:
        while current_interface is not None:
            # Display the current interface
            current_interface.display()
            
            # Get user choice
            choice = current_interface.get_menu_choice(10)  # Max 10 options
            if choice is None:
                break
            
            # Handle the input and get next interface
            next_interface = current_interface.handle_input(choice)
            
            # If logout (None), restart with main menu
            if next_interface is None and not isinstance(current_interface, MainMenu):
                current_interface = MainMenu(session_manager)
            else:
                current_interface = next_interface
    
    except KeyboardInterrupt:
        print("\n\nExiting AgroUSSD...")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        print("Exiting AgroUSSD...")
    
    print("Thank you for using AgroUSSD!")

if __name__ == "__main__":
    main()
