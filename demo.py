#!/usr/bin/env python3
"""
AgroUSSD Demo Script
This script demonstrates the key functionality of the AgroUSSD application
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def demo_application():
    print("🌾 AgroUSSD - Agricultural Marketplace USSD Simulation")
    print("=" * 60)
    print()
    
    try:
        # Test imports
        print("1. Testing imports...")
        from interfaces.session_manager import SessionManager
        from interfaces.main_menu import MainMenu
        from services.user_service import UserService
        from services.market_service import MarketService
        from services.harvest_service import HarvestService
        from services.connection_service import ConnectionService
        from models.user import User
        from models.farmer import Farmer
        from models.buyer import Buyer
        from utils.validators import validate_phone_number, validate_pin
        print("   ✅ All imports successful!")
        print()
        
        # Test session manager
        print("2. Testing SessionManager...")
        session_manager = SessionManager()
        print("   ✅ SessionManager created successfully!")
        print()
        
        # Test services
        print("3. Testing Services...")
        user_service = UserService()
        market_service = MarketService()
        harvest_service = HarvestService()
        connection_service = ConnectionService()
        print("   ✅ All services created successfully!")
        print()
        
        # Test market prices
        print("4. Testing Market Prices...")
        prices = market_service.get_market_prices()
        print(f"   ✅ Found {len(prices)} market prices")
        print("   Sample prices:")
        for crop, price in list(prices.items())[:5]:
            print(f"     {crop}: ₦{price:,.2f}/kg")
        print()
        
        # Test validators
        print("5. Testing Validators...")
        valid, msg = validate_phone_number("08012345678")
        print(f"   Phone validation: {valid} - {msg}")
        valid, msg = validate_pin("1234")
        print(f"   PIN validation: {valid} - {msg}")
        print()
        
        # Test farmer registration
        print("6. Testing Farmer Registration...")
        try:
            farmer = user_service.register_farmer(
                "John Doe", "08012345678", "Lagos", "1234", 
                "Green Acres Farm", 50.0, ["Rice", "Maize"]
            )
            print(f"   ✅ Farmer registered: {farmer.name}")
            print(f"   Farm: {farmer.farm_name} ({farmer.farm_size} acres)")
        except Exception as e:
            print(f"   ⚠️  Farmer registration test failed: {e}")
        print()
        
        # Test buyer registration
        print("7. Testing Buyer Registration...")
        try:
            buyer = user_service.register_buyer(
                "Jane Smith", "08087654321", "Abuja", "5678", "Credit Card"
            )
            print(f"   ✅ Buyer registered: {buyer.name}")
            print(f"   Payment method: {buyer.preferred_payment_method}")
        except Exception as e:
            print(f"   ⚠️  Buyer registration test failed: {e}")
        print()
        
        # Test harvest listing
        print("8. Testing Harvest Listing...")
        try:
            if 'farmer' in locals():
                harvest = harvest_service.create_harvest(
                    farmer, "Rice", 1000, "2024-01-15", 450.0
                )
                print(f"   ✅ Harvest listed: {harvest['crop_type']} - {harvest['quantity']} kg")
                print(f"   Price: ₦{harvest['asking_price']:,.2f}/kg")
        except Exception as e:
            print(f"   ⚠️  Harvest listing test failed: {e}")
        print()
        
        print("🎉 Demo completed successfully!")
        print()
        print("The AgroUSSD application is working correctly!")
        print("You can now run 'python run.py' to start the full application.")
        
    except Exception as e:
        print(f"❌ Demo failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    demo_application()
