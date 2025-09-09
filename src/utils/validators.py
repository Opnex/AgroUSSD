import re
from datetime import datetime

def validate_phone_number(phone):
    """Validate phone number format (11 digits starting with 0)"""
    if not phone:
        return False, "Phone number cannot be empty"
    
    # Remove any non-digit characters
    phone_clean = re.sub(r'\D', '', phone)
    
    if len(phone_clean) != 11:
        return False, "Phone number must be 11 digits"
    
    if not phone_clean.startswith('0'):
        return False, "Phone number must start with 0"
    
    return True, "Valid phone number"

def validate_pin(pin):
    """Validate PIN format (4 digits)"""
    if not pin:
        return False, "PIN cannot be empty"
    
    if not pin.isdigit():
        return False, "PIN must contain only digits"
    
    if len(pin) != 4:
        return False, "PIN must be exactly 4 digits"
    
    return True, "Valid PIN"

def validate_name(name):
    """Validate name format"""
    if not name:
        return False, "Name cannot be empty"
    
    if len(name.strip()) < 2:
        return False, "Name must be at least 2 characters long"
    
    if not re.match(r'^[a-zA-Z\s]+$', name.strip()):
        return False, "Name can only contain letters and spaces"
    
    return True, "Valid name"

def validate_location(location):
    """Validate location format"""
    if not location:
        return False, "Location cannot be empty"
    
    if len(location.strip()) < 2:
        return False, "Location must be at least 2 characters long"
    
    return True, "Valid location"

def validate_farm_size(farm_size):
    """Validate farm size (must be positive number)"""
    try:
        size = float(farm_size)
        if size <= 0:
            return False, "Farm size must be a positive number"
        return True, "Valid farm size"
    except (ValueError, TypeError):
        return False, "Farm size must be a valid number"

def validate_quantity(quantity):
    """Validate quantity (must be positive number)"""
    try:
        qty = float(quantity)
        if qty <= 0:
            return False, "Quantity must be a positive number"
        return True, "Valid quantity"
    except (ValueError, TypeError):
        return False, "Quantity must be a valid number"

def validate_harvest_date(date_string):
    """Validate harvest date format (YYYY-MM-DD)"""
    if not date_string:
        return False, "Harvest date cannot be empty"
    
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True, "Valid harvest date"
    except ValueError:
        return False, "Harvest date must be in YYYY-MM-DD format"

def validate_payment_method(payment_method):
    """Validate payment method"""
    valid_methods = ["Credit Card", "Debit Card", "PayPal", "Bank Transfer", "Cash"]
    if payment_method not in valid_methods:
        return False, f"Invalid payment method. Choose from: {', '.join(valid_methods)}"
    return True, "Valid payment method"

def validate_crop_type(crop_type):
    """Validate crop type"""
    if not crop_type:
        return False, "Crop type cannot be empty"
    
    if len(crop_type.strip()) < 2:
        return False, "Crop type must be at least 2 characters long"
    
    return True, "Valid crop type"
