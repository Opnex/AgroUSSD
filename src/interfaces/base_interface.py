from abc import ABC, abstractmethod

class BaseInterface(ABC):
    """Abstract base class for all USSD interfaces"""
    
    def __init__(self, session_manager):
        self.session_manager = session_manager
    
    @abstractmethod
    def display(self):
        """Display the menu options to the user"""
        pass
    
    @abstractmethod
    def handle_input(self, choice):
        """Handle user input and return the next interface or None to exit"""
        pass
    
    def show_error(self, message):
        """Display an error message"""
        print(f"\n❌ Error: {message}\n")
    
    def show_success(self, message):
        """Display a success message"""
        print(f"\n✅ {message}\n")
    
    def show_info(self, message):
        """Display an info message"""
        print(f"\nℹ️  {message}\n")
    
    def show_warning(self, message):
        """Display a warning message"""
        print(f"\n⚠️  {message}\n")
    
    def pause(self):
        """Pause and wait for user input"""
        input("Press Enter to continue...")
    
    def clear_screen(self):
        """Clear the screen"""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self, title):
        """Print a formatted header"""
        print("=" * 50)
        print(f"  {title}")
        print("=" * 50)
    
    def print_menu(self, options):
        """Print a formatted menu"""
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        print()
    
    def get_menu_choice(self, max_option):
        """Get a valid menu choice from user"""
        while True:
            try:
                choice = input("Enter your choice: ").strip()
                if not choice:
                    print("Please enter a choice.")
                    continue
                
                choice_num = int(choice)
                if 1 <= choice_num <= max_option:
                    return choice_num
                else:
                    print(f"Please enter a number between 1 and {max_option}")
            except ValueError:
                print("Please enter a valid number.")
            except KeyboardInterrupt:
                print("\n\nExiting...")
                return None
