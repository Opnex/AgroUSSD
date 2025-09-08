# connection service search farmers, contact sharing

from src.utils.data_handler import read_json, write_json

CONNECTIONS_FILE = "data/connections.json"

class ConnectionService:
    def __init__(self, user_service):
        """
        user_service: Instance of UserService to access farmer data.
        """
        self.user_service = user_service
        self.connections = self.load_connections()

    def load_connections(self):
        return read_json(CONNECTIONS_FILE)

    def save_connections(self):
        write_json(CONNECTIONS_FILE, self.connections)

    def search_farmers(self, location=None, product_name=None):
        """
        Search farmers by location and/or primary crops.
        Returns list of Farmer objects matching criteria.
        """
        results = []
        for user in self.user_service.users.values():
            if user.get_role() != "Farmer":
                continue
            if location and user.location.lower() != location.lower():
                continue
            if product_name and product_name.lower() not in (crop.lower() for crop in user.primary_crops):
                continue
            results.append(user)
        return results

    def get_farmer_contact(self, farmer_id):
        """
        Returns farmer's phone number if exists.
        """
        farmer = self.user_service.users.get(farmer_id)
        if farmer and farmer.get_role() == "Farmer":
            return farmer.phone
        return None

    def record_connection(self, buyer_id, farmer_id):
        """
        Log a connection between buyer and farmer.
        """
        if buyer_id not in self.connections:
            self.connections[buyer_id] = []
        if farmer_id not in self.connections[buyer_id]:
            self.connections[buyer_id].append(farmer_id)
            self.save_connections()


    

