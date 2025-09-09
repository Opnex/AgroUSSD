# user_service(Registration, Authentication, update)
import uuid
import json
import os
from utils.data_handler import read_json, write_json
from models.farmer import Farmer
from models.buyer import Buyer

USERS_FILE = "data/users.json"

class UserService:
    def __init__(self):
        self.users = self.load_users()
    
    def load_users(self):
        users_data = read_json(USERS_FILE)
        users = {}
        if not users_data:
            return users
            
        for user_id, data in users_data.items():
            role = data.get("role")
            if role == "Farmer":
                user = Farmer(
                    name=data["name"],
                    phone_number=data["phone"],
                    location=data["location"],
                    pin=data["pin"],
                    farm_name=data.get("farm_name", ""),
                    farm_size=data.get("farm_size", 0)
                )
                user.primary_crops = data.get("primary_crops", [])
            elif role == "Buyer":
                user = Buyer(
                    name=data["name"],
                    phone_number=data["phone"],
                    location=data["location"],
                    pin=data["pin"],
                    preferred_payment_method=data.get("preferred_payment_method", "Credit Card")
                )
            else:
                continue
            users[user_id] = user
        return users
  
    def save_users(self):
        users_data = {}
        for user_id, user in self.users.items():
            data = {
                "name": user.name,
                "phone": user.phone_number,
                "location": user.location,
                "pin": user.pin,
                "role": user.get_user_type(),
            }
            if isinstance(user, Farmer):
                data["farm_name"] = user.farm_name
                data["farm_size"] = user.farm_size
                data["primary_crops"] = user.primary_crops
            elif isinstance(user, Buyer):
                data["preferred_payment_method"] = user.preferred_payment_method
            users_data[user_id] = data
        write_json(USERS_FILE, users_data)
    
    def register_farmer(self, name, phone, location, pin, farm_name, farm_size, primary_crops=None):
        user_id = str(uuid.uuid4())
        farmer = Farmer(name, phone, pin, location, farm_name, farm_size)
        if primary_crops:
            farmer.primary_crops = primary_crops
        self.users[user_id] = farmer
        self.save_users()
        return farmer

    def register_buyer(self, name, phone, location, pin, preferred_payment_method="Credit Card"):
        user_id = str(uuid.uuid4())
        buyer = Buyer(name, phone, pin, location, preferred_payment_method)
        self.users[user_id] = buyer
        self.save_users()
        return buyer

    def authenticate_user(self, phone, input_pin):
        for user in self.users.values():
            if user.phone_number == phone and user.verify_pin(input_pin):
                return user
        return None

    def update_user_profile(self, user_id, **kwargs):
        user = self.users.get(user_id)
        if not user:
            return None
        
        if "location" in kwargs:
            user.update_location(kwargs["location"])

        if isinstance(user, Farmer):
            farm_name = kwargs.get("farm_name")
            farm_size = kwargs.get("farm_size")
            primary_crops = kwargs.get("primary_crops")
            user.update_farm_details(farm_name, farm_size, primary_crops)
        elif isinstance(user, Buyer):
            payment_method = kwargs.get("preferred_payment_method")
            if payment_method:
                user.update_payment_method(payment_method)

        self.save_users()
        return user



