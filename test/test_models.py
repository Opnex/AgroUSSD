import os
import sys
import unittest

# Ensure the project's src directory is on sys.path so `models.*` imports work
CURRENT_DIR = os.path.dirname(__file__)
PROJECT_SRC = os.path.normpath(os.path.join(CURRENT_DIR, '..', 'src'))
if PROJECT_SRC not in sys.path:
    sys.path.insert(0, PROJECT_SRC)

from models.user import User
from models.farmer import Farmer
from models.buyer import Buyer
from models.harvest import Harvest
from datetime import datetime

class TestModels(unittest.TestCase):
    def setUp(self):
        self.farmer = Farmer("John Doe", "1234567890", "1234", "Farmville", "Green Acres", 50)
        self.buyer = Buyer("Jane Smith", "0987654321", "5678", "Citytown", "Credit Card")
        self.harvest = Harvest(self.farmer, "Wheat", 1000, "2023-10-01")

    def test_user_str(self):
        self.assertEqual(str(self.farmer), "Name: John Doe, Phone: 1234567890, Location: Farmville")
        self.assertEqual(str(self.buyer), "Name: Jane Smith, Phone: 0987654321, Location: Citytown")

    def test_farmer_display_info(self):
        expected_info = "Name: John Doe, Phone: 1234567890, Location: Farmville, Farm Name: Green Acres, Farm Size: 50 acres"
        self.assertEqual(self.farmer.display_info(), expected_info)

    def test_buyer_display_info(self):
        expected_info = "Name: Jane Smith, Phone: 0987654321, Location: Citytown, Preferred Payment Method: Credit Card"
        self.assertEqual(self.buyer.display_info(), expected_info)

    def test_update_location(self):
        self.farmer.update_location("New Farmville")
        self.assertEqual(self.farmer.location, "New Farmville")

    def test_verify_pin(self):
        self.assertTrue(self.farmer.verify_pin("1234"))
        self.assertFalse(self.farmer.verify_pin("0000"))

    def test_update_farm_details(self):
        self.farmer.update_farm_details(new_farm_name="Sunny Fields", new_farm_size=75)
        self.assertEqual(self.farmer.farm_name, "Sunny Fields")
        self.assertEqual(self.farmer.farm_size, 75)

    def test_validate_farm_size(self):
        with self.assertRaises(ValueError):
            self.farmer.farm_size = -10
            self.farmer.validate_farm_size()

    def test_update_payment_method(self):
        self.buyer.update_payment_method("PayPal")
        self.assertEqual(self.buyer.preferred_payment_method, "PayPal")

    def test_validate_payment_method(self):
        with self.assertRaises(ValueError):
            self.buyer.preferred_payment_method = "Cash"
            self.buyer.validate_payment_method()
    def test_harvest_display_info(self):
        expected_info = "Farmer: John Doe, Crop Type: Wheat, Quantity: 1000 kg, Harvest Date: 2023-10-01"
        self.assertEqual(self.harvest.display_info(), expected_info)
    def test_validate_quantity(self):
        with self.assertRaises(ValueError):
            Harvest(self.farmer, "Corn", -500, "2023-10-01")
    def test_validate_harvest_date(self):
        with self.assertRaises(ValueError):
            Harvest(self.farmer, "Corn", 500, "10-01-2023")

if __name__ == '__main__':
    unittest.main()


    