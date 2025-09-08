import logging
from models.user import User

logger = logging.getLogger(__name__)

class Farmer(User):
    def __init__(self, name, phone_number, pin, location, farm_name, farm_size):
        super().__init__(name, phone_number, pin, location)
        self.farm_name = farm_name
        self.farm_size = farm_size  # in acres

    def get_user_type(self):
        return "Farmer"

    def display_info(self):
        user_info = super().__str__()
        return f"{user_info}, Farm Name: {self.farm_name}, Farm Size: {self.farm_size} acres"
    
    def update_farm_details(self, new_farm_name=None, new_farm_size=None):
        if new_farm_name:
            self.farm_name = new_farm_name
            logger.info("Farm name updated to %s", self.farm_name)
        if new_farm_size:
            if new_farm_size <= 0:
                raise ValueError("Farm size must be a positive number.")
            self.farm_size = new_farm_size
            logger.info("Farm size updated to %s acres", self.farm_size)

    def validate_farm_size(self):
        if self.farm_size <= 0:
            raise ValueError("Farm size must be a positive number.")
        logger.info("Farm size of %s acres is valid.", self.farm_size)