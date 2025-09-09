from interfaces.base_interface import BaseInterface
from services.market_service import MarketService
from services.harvest_service import HarvestService
from utils.validators import validate_crop_type, validate_quantity, validate_harvest_date

class FarmerMenu(BaseInterface):
    def __init__(self, session_manager):
        super().__init__(session_manager)
        self.market_service = MarketService()
        self.harvest_service = HarvestService()

    def display(self):
        self.clear_screen()
        user_info = self.session_manager.get_user_info()
        self.print_header(f"Farmer Dashboard - {user_info['name']}")
        
        print(f"Phone: {user_info['phone']}")
        print(f"Location: {user_info['location']}")
        print(f"Farm: {self.session_manager.current_user.farm_name}")
        print(f"Farm Size: {self.session_manager.current_user.farm_size} acres")
        print()
        
        options = [
            "Check Market Prices",
            "List New Harvest",
            "View My Listings",
            "Update Profile",
            "Logout"
        ]
        
        self.print_menu(options)

    def handle_input(self, choice):
        if choice == 1:
            return self._handle_market_prices()
        elif choice == 2:
            return self._handle_list_harvest()
        elif choice == 3:
            return self._handle_view_listings()
        elif choice == 4:
            return self._handle_update_profile()
        elif choice == 5:
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

    def _handle_list_harvest(self):
        self.clear_screen()
        self.print_header("List New Harvest")
        
        crop_type = input("Enter crop type: ").strip()
        is_valid, message = validate_crop_type(crop_type)
        if not is_valid:
            self.show_error(message)
            self.pause()
            return self
        
        quantity = input("Enter quantity in kg: ").strip()
        is_valid, message = validate_quantity(quantity)
        if not is_valid:
            self.show_error(message)
            self.pause()
            return self
        
        quantity = float(quantity)
        
        harvest_date = input("Enter harvest date (YYYY-MM-DD): ").strip()
        is_valid, message = validate_harvest_date(harvest_date)
        if not is_valid:
            self.show_error(message)
            self.pause()
            return self
        
        asking_price = input("Enter your asking price per kg: ").strip()
        try:
            asking_price = float(asking_price)
            if asking_price <= 0:
                raise ValueError()
        except ValueError:
            self.show_error("Asking price must be a positive number.")
            self.pause()
            return self
        
        try:
            harvest = self.harvest_service.create_harvest(
                self.session_manager.current_user,
                crop_type,
                quantity,
                harvest_date,
                asking_price
            )
            self.show_success(f"Harvest listed successfully!")
            self.show_info(f"Crop: {crop_type}")
            self.show_info(f"Quantity: {quantity} kg")
            self.show_info(f"Price: ₦{asking_price:,.2f} per kg")
            self.show_info(f"Total Value: ₦{quantity * asking_price:,.2f}")
        except Exception as e:
            self.show_error(f"Failed to list harvest: {str(e)}")
        
        self.pause()
        return self

    def _handle_view_listings(self):
        self.clear_screen()
        self.print_header("My Harvest Listings")
        
        listings = self.harvest_service.get_farmer_listings(self.session_manager.current_user.phone_number)
        if not listings:
            self.show_info("You have no active listings.")
        else:
            print("Your active listings:")
            print("-" * 60)
            for i, listing in enumerate(listings, 1):
                print(f"{i}. {listing['crop_type']} - {listing['quantity']} kg")
                print(f"   Price: ₦{listing['asking_price']:,.2f} per kg")
                print(f"   Harvest Date: {listing['harvest_date']}")
                print(f"   Total Value: ₦{listing['quantity'] * listing['asking_price']:,.2f}")
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
        print(f"Farm Name: {self.session_manager.current_user.farm_name}")
        print(f"Farm Size: {self.session_manager.current_user.farm_size} acres")
        print(f"Primary Crops: {', '.join(self.session_manager.current_user.primary_crops)}")
        print()
        
        print("What would you like to update?")
        options = [
            "Location",
            "Farm Name",
            "Farm Size",
            "Primary Crops",
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
            new_farm_name = input("Enter new farm name: ").strip()
            if new_farm_name:
                self.session_manager.current_user.update_farm_details(new_farm_name=new_farm_name)
                self.show_success("Farm name updated successfully!")
        elif choice == 3:
            new_farm_size = input("Enter new farm size in acres: ").strip()
            try:
                new_farm_size = float(new_farm_size)
                if new_farm_size > 0:
                    self.session_manager.current_user.update_farm_details(new_farm_size=new_farm_size)
                    self.show_success("Farm size updated successfully!")
                else:
                    self.show_error("Farm size must be positive.")
            except ValueError:
                self.show_error("Invalid farm size.")
        elif choice == 4:
            new_crops = input("Enter new primary crops (comma-separated): ").strip()
            crops_list = [crop.strip() for crop in new_crops.split(",")] if new_crops else []
            self.session_manager.current_user.update_farm_details(new_primary_crops=crops_list)
            self.show_success("Primary crops updated successfully!")
        elif choice == 5:
            return self
        
        self.pause()
        return self

    def _handle_logout(self):
        self.session_manager.logout()
        self.show_success("Logged out successfully!")
        self.pause()
        # Return None to go back to main menu
        return None
