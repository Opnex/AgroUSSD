#!/usr/bin/env python3
"""
Test script to verify imports work correctly
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    try:
        print("Testing imports...")
        
        # Test basic imports
        from interfaces.session_manager import SessionManager
        print("✅ SessionManager imported")
        
        from interfaces.main_menu import MainMenu
        print("✅ MainMenu imported")
        
        from services.user_service import UserService
        print("✅ UserService imported")
        
        from services.market_service import MarketService
        print("✅ MarketService imported")
        
        from models.user import User
        print("✅ User model imported")
        
        from models.farmer import Farmer
        print("✅ Farmer model imported")
        
        from models.buyer import Buyer
        print("✅ Buyer model imported")
        
        from utils.validators import validate_phone_number
        print("✅ Validators imported")
        
        print("\n🎉 All imports successful!")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    test_imports()
