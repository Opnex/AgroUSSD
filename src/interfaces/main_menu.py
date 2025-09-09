from interfaces.base_interface import BaseInterface
from interfaces.farmer_menu import FarmerMenu
from interfaces.buyer_menu import BuyerMenu
from services.user_service import UserService
from utils.validators import validate_phone_number, validate_pin, validate_name, validate_location

class MainMenu(BaseInterface):
    def __init__(self, session_manager):
        super().__init__(session_manager)
        self.user_service = UserService()

    def display(self):
        self.clear_screen()
        self.print_header("AgroUSSD - Agricultural Marketplace")
        print("Welcome to AgroUSSD - Your Direct Link to Agricultural Markets!")
        print("\nThis system helps farmers and buyers connect directly,")
        print("cutting out middlemen and ensuring fair prices for everyone.")
        print()
        
        options = [
            "Login",
            "Register as Farmer",
            "Register as Buyer",
            "Exit"
        ]
        
        self.print_menu(options)

    def handle_input(self, choice):
        if choice == 1:
            return self._handle_login()
        elif choice == 2:
            return self._handle_farmer_registration()
        elif choice == 3:
            return self._handle_buyer_registration()
        elif choice == 4:
            return None  # Exit
        else:
            self.show_error("Invalid choice. Please try again.")
            return self

    def _handle_login(self):
        self.clear_screen()
        self.print_header("Login")
        
        phone = input("Enter your phone number: ").strip()
        is_valid, message = validate_phone_number(phone)
        if not is_valid:
            self.show_error(message)
            self.pause()
            return self
        
        pin = input("Enter your PIN: ").strip()
        is_valid, message = validate_pin(pin)
        if not is_valid:
            self.show_error(message)
            self.pause()
            return self
        
        user = self.user_service.authenticate_user(phone, pin)
        if user:
            self.session_manager.login(user)
            self.show_success(f"Welcome back, {user.name}!")
            self.pause()
            
            if user.get_user_type() == "Farmer":
                return FarmerMenu(self.session_manager)
            else:
                return BuyerMenu(self.session_manager)
        else:
            self.show_error("Invalid phone number or PIN.")
            self.pause()
            return self

    def _handle_farmer_registration(self):
        self.clear_screen()
        self.print_header("Farmer Registration")
        
        # Get farmer details
        name = input("Enter your full name: ").strip()
        is_valid, message = validate_name(name)
        if not is_valid:
            self.show_error(message)
            self.pause()
            return self
        
        phone = input("Enter your phone number (11 digits starting with 0): ").strip()
        is_valid, message = validate_phone_number(phone)
        if not is_valid:
            self.show_error(message)
            self.pause()
            return self
        
        location = input("Enter your location: ").strip()
        is_valid, message = validate_location(location)
        if not is_valid:
            self.show_error(message)
            self.pause()
            return self
        
        pin = input("Enter a 4-digit PIN: ").strip()
        is_valid, message = validate_pin(pin)
        if not is_valid:
            self.show_error(message)
            self.pause()
            return self
        
        farm_name = input("Enter your farm name: ").strip()
        if not farm_name:
            self.show_error("Farm name cannot be empty.")
            self.pause()
            return self
        
        farm_size = input("Enter your farm size in acres: ").strip()
        try:
            farm_size = float(farm_size)
            if farm_size <= 0:
                raise ValueError()
        except ValueError:
            self.show_error("Farm size must be a positive number.")
            self.pause()
            return self
        
        primary_crops = input("Enter your primary crops (comma-separated): ").strip()
        crops_list = [crop.strip() for crop in primary_crops.split(",")] if primary_crops else []
        
        try:
            farmer = self.user_service.register_farmer(
                name, phone, location, pin, farm_name, farm_size, crops_list
            )
            self.session_manager.login(farmer)
            self.show_success(f"Registration successful! Welcome, {farmer.name}!")
            self.pause()
            return FarmerMenu(self.session_manager)
        except Exception as e:
            self.show_error(f"Registration failed: {str(e)}")
            self.pause()
            return self

    def _handle_buyer_registration(self):
        self.clear_screen()
        self.print_header("Buyer Registration")
        
        # Get buyer details
        name = input("Enter your full name: ").strip()
        is_valid, message = validate_name(name)
        if not is_valid:
            self.show_error(message)
            self.pause()
            return self
        
        phone = input("Enter your phone number (11 digits starting with 0): ").strip()
        is_valid, message = validate_phone_number(phone)
        if not is_valid:
            self.show_error(message)
            self.pause()
            return self
        
        location = input("Enter your location: ").strip()
        is_valid, message = validate_location(location)
        if not is_valid:
            self.show_error(message)
            self.pause()
            return self
        
        pin = input("Enter a 4-digit PIN: ").strip()
        is_valid, message = validate_pin(pin)
        if not is_valid:
            self.show_error(message)
            self.pause()
            return self
        
        print("\nPreferred Payment Methods:")
        payment_options = ["Credit Card", "Debit Card", "PayPal", "Bank Transfer", "Cash"]
        self.print_menu(payment_options)
        
        choice = self.get_menu_choice(len(payment_options))
        if choice is None:
            return self
        
        preferred_payment = payment_options[choice - 1]
        
        try:
            buyer = self.user_service.register_buyer(
                name, phone, location, pin, preferred_payment
            )
            self.session_manager.login(buyer)
            self.show_success(f"Registration successful! Welcome, {buyer.name}!")
            self.pause()
            return BuyerMenu(self.session_manager)
        except Exception as e:
            self.show_error(f"Registration failed: {str(e)}")
            self.pause()
            return self
