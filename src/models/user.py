import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

class User(ABC):
    def __init__(self, name, phone_number, pin, location):
        self.name = name
        self.phone_number = phone_number
        self.pin = pin
        self.location = location

    @abstractmethod
    def get_user_type(self):
        pass

    @abstractmethod
    def display_info(self):
        pass

    def update_location(self, new_location):
        self.location = new_location
        logger.info("Location updated to %s", self.location)

    def verify_pin(self, input_pin):
        return self.pin == input_pin
    
    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Location: {self.location}"  