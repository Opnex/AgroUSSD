from interfaces.base_interface import BaseInterface
from services.market_service import MarketService
from services.harvest_service import HarvestService
from services.connection_service import ConnectionService

class BuyerMenu(BaseInterface):
    def __init__(self, session_manager):
        super().__init__(session_manager)
        self.market_service = MarketService()
        self.harvest_service = HarvestService()
        self.connection_service = ConnectionService()

    def display(self):
        self.clear_screen()
        user_info = self.session_manager.get_user_info()
        self.print_header(f"Buyer Dashboard - {user_info['name']}")
        
        print(f"Phone: {user_info['phone']}")
        print(f"Location: {user_info['location']}")
        print(f"Payment Method: {self.session_manager.current_user.preferred_payment_method}")
        print()
        
        options = [
            "Check Market Prices",
            "Browse Available Crops",
            "Search by Crop Type",
            "Search by Location",
            "View My Connections",
            "Update Profile",
            "Logout"
        ]
        
        self.print_menu(options)

    def handle_input(self, choice):
        if choice == 1:
            return self._handle_market_prices()
        elif choice == 2:
            return self._handle_browse_crops()
        elif choice == 3:
            return self._handle_search_by_crop()
        elif choice == 4:
            return self._handle_search_by_location()
        elif choice == 5:
            return self._handle_view_connections()
        elif choice == 6:
            return self._handle_update_profile()
        elif choice == 7:
            return self._handle_logout()
        else:
            self.show_error("Invalid choice. Please try again.")
            return self

    def _handle_market_prices(self):
        self.clear_screen()
        self.print_header("Current Market Prices")
        
        prices = self.market_service.get_market_prices()
        if not prices:
            self.show_warning("No market price data available.")
        else:
            print("Current market prices per kg:")
            print("-" * 40)
            for crop, price in prices.items():
                print(f"{crop}: ₦{price:,.2f}")
        
        self.pause()
        return self

    def _handle_browse_crops(self):
        self.clear_screen()
        self.print_header("Available Crops")
        
        listings = self.harvest_service.get_all_listings()
        if not listings:
            self.show_info("No crops available at the moment.")
        else:
            print("Available crops:")
            print("-" * 80)
            for i, listing in enumerate(listings, 1):
                print(f"{i}. {listing['crop_type']} - {listing['quantity']} kg")
                print(f"   Farmer: {listing['farmer_name']} ({listing['farmer_phone']})")
                print(f"   Location: {listing['farmer_location']}")
                print(f"   Price: ₦{listing['asking_price']:,.2f} per kg")
                print(f"   Harvest Date: {listing['harvest_date']}")
                print(f"   Total Value: ₦{listing['quantity'] * listing['asking_price']:,.2f}")
                print()
            
            print("Would you like to connect with any farmer?")
            if self.confirm_action("Connect with a farmer"):
                self._handle_farmer_connection(listings)
        
        self.pause()
        return self

    def _handle_search_by_crop(self):
        self.clear_screen()
        self.print_header("Search by Crop Type")
        
        crop_type = input("Enter crop type to search for: ").strip()
        if not crop_type:
            self.show_error("Crop type cannot be empty.")
            self.pause()
            return self
        
        listings = self.harvest_service.search_by_crop(crop_type)
        if not listings:
            self.show_info(f"No {crop_type} available at the moment.")
        else:
            print(f"Available {crop_type}:")
            print("-" * 80)
            for i, listing in enumerate(listings, 1):
                print(f"{i}. {listing['quantity']} kg")
                print(f"   Farmer: {listing['farmer_name']} ({listing['farmer_phone']})")
                print(f"   Location: {listing['farmer_location']}")
                print(f"   Price: ₦{listing['asking_price']:,.2f} per kg")
                print(f"   Harvest Date: {listing['harvest_date']}")
                print(f"   Total Value: ₦{listing['quantity'] * listing['asking_price']:,.2f}")
                print()
            
            print("Would you like to connect with any farmer?")
            if self.confirm_action("Connect with a farmer"):
                self._handle_farmer_connection(listings)
        
        self.pause()
        return self

    def _handle_search_by_location(self):
        self.clear_screen()
        self.print_header("Search by Location")
        
        location = input("Enter location to search in: ").strip()
        if not location:
            self.show_error("Location cannot be empty.")
            self.pause()
            return self
        
        listings = self.harvest_service.search_by_location(location)
        if not listings:
            self.show_info(f"No crops available in {location}.")
        else:
            print(f"Available crops in {location}:")
            print("-" * 80)
            for i, listing in enumerate(listings, 1):
                print(f"{i}. {listing['crop_type']} - {listing['quantity']} kg")
                print(f"   Farmer: {listing['farmer_name']} ({listing['farmer_phone']})")
                print(f"   Price: ₦{listing['asking_price']:,.2f} per kg")
                print(f"   Harvest Date: {listing['harvest_date']}")
                print(f"   Total Value: ₦{listing['quantity'] * listing['asking_price']:,.2f}")
                print()
            
            print("Would you like to connect with any farmer?")
            if self.confirm_action("Connect with a farmer"):
                self._handle_farmer_connection(listings)
        
        self.pause()
        return self

    def _handle_farmer_connection(self, listings):
        try:
            choice = input("Enter the number of the listing you want to connect with: ").strip()
            choice_num = int(choice)
            if 1 <= choice_num <= len(listings):
                listing = listings[choice_num - 1]
                connection = self.connection_service.create_connection(
                    self.session_manager.current_user,
                    listing['farmer_phone'],
                    listing['crop_type'],
                    listing['quantity'],
                    listing['asking_price']
                )
                self.show_success("Connection request sent successfully!")
                self.show_info(f"Farmer: {listing['farmer_name']}")
                self.show_info(f"Phone: {listing['farmer_phone']}")
                self.show_info(f"Crop: {listing['crop_type']}")
                self.show_info(f"Quantity: {listing['quantity']} kg")
                self.show_info(f"Price: ₦{listing['asking_price']:,.2f} per kg")
            else:
                self.show_error("Invalid selection.")
        except (ValueError, IndexError):
            self.show_error("Invalid selection.")

    def _handle_view_connections(self):
        self.clear_screen()
        self.print_header("My Connections")
        
        connections = self.connection_service.get_buyer_connections(self.session_manager.current_user.phone_number)
        if not connections:
            self.show_info("You have no connections yet.")
        else:
            print("Your connections:")
            print("-" * 80)
            for i, connection in enumerate(connections, 1):
                print(f"{i}. {connection['crop_type']} - {connection['quantity']} kg")
                print(f"   Farmer: {connection['farmer_name']} ({connection['farmer_phone']})")
                print(f"   Price: ₦{connection['asking_price']:,.2f} per kg")
                print(f"   Status: {connection['status']}")
                print(f"   Date: {connection['created_date']}")
                print()
        
        self.pause()
        return self

    def _handle_update_profile(self):
        self.clear_screen()
        self.print_header("Update Profile")
        
        print("Current profile information:")
        print(f"Name: {self.session_manager.current_user.name}")
        print(f"Phone: {self.session_manager.current_user.phone_number}")
        print(f"Location: {self.session_manager.current_user.location}")
        print(f"Payment Method: {self.session_manager.current_user.preferred_payment_method}")
        print()
        
        print("What would you like to update?")
        options = [
            "Location",
            "Payment Method",
            "Back to Main Menu"
        ]
        
        self.print_menu(options)
        choice = self.get_menu_choice(len(options))
        if choice is None:
            return self
        
        if choice == 1:
            new_location = input("Enter new location: ").strip()
            if new_location:
                self.session_manager.current_user.update_location(new_location)
                self.show_success("Location updated successfully!")
        elif choice == 2:
            print("\nSelect new payment method:")
            payment_options = ["Credit Card", "Debit Card", "PayPal", "Bank Transfer", "Cash"]
            self.print_menu(payment_options)
            choice = self.get_menu_choice(len(payment_options))
            if choice is not None:
                new_payment = payment_options[choice - 1]
                self.session_manager.current_user.update_payment_method(new_payment)
                self.show_success("Payment method updated successfully!")
        elif choice == 3:
            return self
        
        self.pause()
        return self

    def _handle_logout(self):
        self.session_manager.logout()
        self.show_success("Logged out successfully!")
        self.pause()
        # Return None to go back to main menu
        return None
