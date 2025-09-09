# connection service search farmers, contact sharing

import uuid
from datetime import datetime
from utils.data_handler import read_json, write_json

class ConnectionService:
    def __init__(self):
        self.connections_file = "data/connections.json"

    def create_connection(self, buyer, farmer_phone, crop_type, quantity, asking_price):
        """Create a connection between buyer and farmer"""
        connection_id = str(uuid.uuid4())
        connection_data = {
            "connection_id": connection_id,
            "buyer_phone": buyer.phone_number,
            "buyer_name": buyer.name,
            "farmer_phone": farmer_phone,
            "crop_type": crop_type,
            "quantity": quantity,
            "asking_price": asking_price,
            "status": "pending",
            "created_date": datetime.now().strftime("%Y-%m-%d"),
            "total_value": quantity * asking_price
        }
        
        # Load existing connections
        connections = read_json(self.connections_file)
        if not connections:
            connections = {}
        
        connections[connection_id] = connection_data
        write_json(self.connections_file, connections)
        
        return connection_data

    def get_buyer_connections(self, buyer_phone):
        """Get all connections for a specific buyer"""
        connections = read_json(self.connections_file)
        if not connections:
            return []
        
        return [conn for conn in connections.values() 
                if conn.get("buyer_phone") == buyer_phone]

    def get_farmer_connections(self, farmer_phone):
        """Get all connections for a specific farmer"""
        connections = read_json(self.connections_file)
        if not connections:
            return []
        
        return [conn for conn in connections.values() 
                if conn.get("farmer_phone") == farmer_phone]

    def update_connection_status(self, connection_id, status):
        """Update the status of a connection"""
        connections = read_json(self.connections_file)
        if connection_id in connections:
            connections[connection_id]["status"] = status
            connections[connection_id]["updated_date"] = datetime.now().strftime("%Y-%m-%d")
            write_json(self.connections_file, connections)
            return True
        return False

    def get_connection_by_id(self, connection_id):
        """Get a specific connection by ID"""
        connections = read_json(self.connections_file)
        return connections.get(connection_id)

    def get_pending_connections(self, farmer_phone):
        """Get pending connections for a farmer"""
        connections = read_json(self.connections_file)
        if not connections:
            return []
        
        return [conn for conn in connections.values() 
                if conn.get("farmer_phone") == farmer_phone and conn.get("status") == "pending"]

    def accept_connection(self, connection_id):
        """Accept a connection request"""
        return self.update_connection_status(connection_id, "accepted")

    def reject_connection(self, connection_id):
        """Reject a connection request"""
        return self.update_connection_status(connection_id, "rejected")

    def complete_connection(self, connection_id):
        """Mark a connection as completed"""
        return self.update_connection_status(connection_id, "completed")
