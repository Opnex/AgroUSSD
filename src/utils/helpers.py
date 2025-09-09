import os
import sys
from datetime import datetime

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    """Print a formatted header"""
    print("=" * 50)
    print(f"  {title}")
    print("=" * 50)

def print_menu(options):
    """Print a formatted menu"""
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    print()

def get_user_input(prompt):
    """Get user input with error handling"""
    try:
        return input(prompt).strip()
    except KeyboardInterrupt:
        print("\n\nExiting...")
        sys.exit(0)
    except EOFError:
        print("\n\nExiting...")
        sys.exit(0)

def get_menu_choice(max_option):
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
            sys.exit(0)

def format_currency(amount):
    """Format amount as currency"""
    return f"₦{amount:,.2f}"

def format_date(date_string):
    """Format date string for display"""
    try:
        date_obj = datetime.strptime(date_string, '%Y-%m-%d')
        return date_obj.strftime('%B %d, %Y')
    except ValueError:
        return date_string

def format_phone(phone):
    """Format phone number for display"""
    if len(phone) == 11 and phone.startswith('0'):
        return f"{phone[:4]} {phone[4:7]} {phone[7:]}"
    return phone

def confirm_action(message):
    """Ask user to confirm an action"""
    while True:
        response = get_user_input(f"{message} (y/n): ").lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def pause():
    """Pause and wait for user to press Enter"""
    get_user_input("Press Enter to continue...")

def print_error(message):
    """Print an error message"""
    print(f"❌ Error: {message}")

def print_success(message):
    """Print a success message"""
    print(f"✅ {message}")

def print_info(message):
    """Print an info message"""
    print(f"ℹ️  {message}")

def print_warning(message):
    """Print a warning message"""
    print(f"⚠️  {message}")
