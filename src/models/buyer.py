import logging
from models.user import User

logger = logging.getLogger(__name__)

class Buyer(User):
    def __init__(self, name, phone_number, pin, location, preferred_payment_method):
        super().__init__(name, phone_number, pin, location)
        self.preferred_payment_method = preferred_payment_method

    def get_user_type(self):
        return "Buyer"

    def display_info(self):
        user_info = super().__str__()
        return f"{user_info}, Preferred Payment Method: {self.preferred_payment_method}"
    
    def update_payment_method(self, new_payment_method):
        self.preferred_payment_method = new_payment_method
        logger.info("Payment method updated to %s", self.preferred_payment_method)

    def validate_payment_method(self):
        valid_methods = ["Credit Card", "Debit Card", "PayPal", "Bank Transfer"]
        if self.preferred_payment_method not in valid_methods:
            raise ValueError(f"Invalid payment method. Choose from: {', '.join(valid_methods)}")
        logger.info("Payment method %s is valid.", self.preferred_payment_method)