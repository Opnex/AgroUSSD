import logging
from models.farmer import Farmer

logger = logging.getLogger(__name__)

class Harvest:
    def __init__(self, farmer: Farmer, crop_type, quantity, harvest_date):
        if not isinstance(farmer, Farmer):
            raise ValueError("harvester must be an instance of Farmer")
        self.farmer = farmer
        self.crop_type = crop_type
        self.quantity = quantity  # in kilograms
        self.harvest_date = harvest_date  # expected to be a string in 'YYYY-MM-DD' format

        self.validate_quantity()
        self.validate_harvest_date()

    def validate_quantity(self):
        if self.quantity <= 0:
            raise ValueError("Quantity must be a positive number.")
        logger.info("Quantity of %s kg is valid.", self.quantity)

    def validate_harvest_date(self):
        from datetime import datetime
        try:
            datetime.strptime(self.harvest_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Harvest date must be in 'YYYY-MM-DD' format.")
        logger.info("Harvest date %s is valid.", self.harvest_date)

    def display_info(self):
        return (f"Farmer: {self.farmer.name}, Crop Type: {self.crop_type}, "
                f"Quantity: {self.quantity} kg, Harvest Date: {self.harvest_date}")