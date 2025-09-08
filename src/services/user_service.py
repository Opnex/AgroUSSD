# user_service(Registration, Authentication, update)
import uuid
import json
from src.utils.data_handler import read_json, write_json
from src.models.farmer import Farmer
from src.models.buyer import Buyer

USERS_FILE = "data/users.json"

class Userservice:
  def __init__(self):
    self.users = self.load_users()
  
  def load_users(self):
    users_data = read_json(USERS_FILE)
    users = {}
    for user_id, data in users_data.items():
      role = data.get("role")
      if role == "Farmer":
        user = Farmer(
          user_id = user_id,
          name = data["name"],
          phone = data["phone"],
          loaction = data["location"],
          pin = data["pin"],
          farm_size = data.get("farm_size"),
          primary_crops = data.get("primary_crops", [])
        )
      elif role =="Buyer":
        user = Buyer(
          user_id=user_id,
          name=data["name"],
          phone=data["phone"],
          location=data["loaction"],
          pin=data["pin"]
        )
      else:
        continue
      users[user_id]=user
    return users
  
  def save_users(self):
    users_data={}
    for user_id, user in self.users.items():
      data={
        "name":user.name,
        "phone":user.name,
        "location":user.location,
        "pin":user.pin,
        "role":user.get_role(),
      }
      if isinstance(user, Farmer):
        data["farm_size"]=user.farm_size
        data["primary_crops"]=user.primary_crops
      users_data[user_id]=data
    write_json(USERS_FILE, users_data)
  
  def register_farmer(self, name, phone, location, pin, farm_size, primary_crops):
        user_id = str(uuid.uuid4())
        farmer = Farmer(user_id, name, phone, location, pin, farm_size, primary_crops)
        self.users[user_id] = farmer
        self.save_users()
        return farmer

  def register_buyer(self, name, phone, location, pin):
        user_id = str(uuid.uuid4())
        buyer = Buyer(user_id, name, phone, location, pin)
        self.users[user_id] = buyer
        self.save_users()
        return buyer

  def authenticate_user(self, phone, input_pin):
        for user in self.users.values():
            if user.phone == phone and user.authenticate(input_pin):
                return user
        return None

  def update_user_profile(self, user_id, **kwargs):
        user = self.users.get(user_id)
        if not user:
            return None
        phone = kwargs.get("phone")
        location = kwargs.get("location")
        user.update_contact(phone=phone, location=location)

        if isinstance(user, Farmer):
            farm_size = kwargs.get("farm_size")
            primary_crops = kwargs.get("primary_crops")
            user.update_farming_details(farm_size=farm_size, primary_crops=primary_crops)

        self.save_users()
        return user



