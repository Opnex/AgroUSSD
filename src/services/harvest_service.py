# Harvest service harvest recording, inventory tracking

import uuid
from src.utils.data_handler import read_json, write_json
from src.models.harvest import Harvest

HARVESTS_FILE = "data/harvests.json"

class HarvestService:
    def __init__(self):
        self.harvests = self.load_harvests()

    def load_harvests(self):
        data = read_json(HARVESTS_FILE)
        harvests = {}
        for h_id, h_data in data.items():
            harvest = Harvest(
                harvest_id=h_id,
                farmer_id=h_data["farmer_id"],
                product_id=h_data["product_id"],
                quantity=h_data["quantity"],
                quality=h_data["quality"],
                asking_price=h_data["asking_price"],
                date=h_data["date"]
            )
            harvests[h_id] = harvest
        return harvests
    
    def save_harvests(self):
        data = {h_id: harvest.get_summary() for h_id, harvest in self.harvests.items()}
        write_json(HARVESTS_FILE, data)

    def record_harvest(self, farmer_id, product_id, quantity, quality, asking_price, data):
        harvest_id =str(uuid.uuid4())
        new_harvest=Harvest(harvest_id,farmer_id, product_id, quantity, asking_price, data)
        self.harvests[harvest_id]=new_harvest
        self.save_harvests()
        return new_harvest
    
    def get_inventory_by_format(self, farmer_id):
        """
        Returns all harvest entries for a famer.
        """
        return[h for h in self.harvest.values() if h.farmer_id==farmer_id]
    
    def get_all_inventory(self):
        """
        Returns all harvest entries.
        """
        return list(self.harvests.values())
    