# Harvest service harvest recording, inventory tracking

import uuid
from datetime import datetime
from utils.data_handler import read_json, write_json
from models.harvest import Harvest

HARVESTS_FILE = "data/harvests.json"

class HarvestService:
    def __init__(self):
        self.harvests_file = HARVESTS_FILE

    def create_harvest(self, farmer, crop_type, quantity, harvest_date, asking_price):
        """Create a new harvest listing"""
        harvest_id = str(uuid.uuid4())
        harvest_data = {
            "harvest_id": harvest_id,
            "farmer_phone": farmer.phone_number,
            "farmer_name": farmer.name,
            "farmer_location": farmer.location,
            "crop_type": crop_type,
            "quantity": quantity,
            "harvest_date": harvest_date,
            "asking_price": asking_price,
            "created_date": datetime.now().strftime("%Y-%m-%d"),
            "status": "available"
        }
        
        # Load existing harvests
        harvests = read_json(self.harvests_file)
        if not harvests:
            harvests = {}
        
        harvests[harvest_id] = harvest_data
        write_json(self.harvests_file, harvests)
        
        return harvest_data

    def get_all_listings(self):
        """Get all available harvest listings"""
        harvests = read_json(self.harvests_file)
        if not harvests:
            return []
        
        # Filter only available listings
        return [harvest for harvest in harvests.values() if harvest.get("status") == "available"]

    def get_farmer_listings(self, farmer_phone):
        """Get all listings for a specific farmer"""
        harvests = read_json(self.harvests_file)
        if not harvests:
            return []
        
        return [harvest for harvest in harvests.values() 
                if harvest.get("farmer_phone") == farmer_phone and harvest.get("status") == "available"]

    def search_by_crop(self, crop_type):
        """Search listings by crop type"""
        all_listings = self.get_all_listings()
        return [listing for listing in all_listings 
                if listing.get("crop_type", "").lower() == crop_type.lower()]

    def search_by_location(self, location):
        """Search listings by farmer location"""
        all_listings = self.get_all_listings()
        return [listing for listing in all_listings 
                if location.lower() in listing.get("farmer_location", "").lower()]

    def get_harvest_by_id(self, harvest_id):
        """Get a specific harvest by ID"""
        harvests = read_json(self.harvests_file)
        return harvests.get(harvest_id)

    def update_harvest_status(self, harvest_id, status):
        """Update the status of a harvest listing"""
        harvests = read_json(self.harvests_file)
        if harvest_id in harvests:
            harvests[harvest_id]["status"] = status
            write_json(self.harvests_file, harvests)
            return True
        return False

    def remove_harvest(self, harvest_id):
        """Remove a harvest listing"""
        harvests = read_json(self.harvests_file)
        if harvest_id in harvests:
            del harvests[harvest_id]
            write_json(self.harvests_file, harvests)
            return True
        return False
    