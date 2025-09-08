import logging

logger = logging.getLogger(__name__)


class Product:
    def __init__(self, name, unit, price_per_unit, available_quantity):
        self.name = name
        self.unit = unit  # e.g., 'kg', 'ton', 'bag'
        self.price_per_unit = price_per_unit  # numeric
        self.available_quantity = available_quantity  # numeric

        self.validate_name()
        self.validate_unit()
        self.validate_price()
        self.validate_quantity()

    def validate_name(self):
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("Product name must be a non-empty string.")
        logger.info("Product name '%s' is valid.", self.name)

    def validate_unit(self):
        if not isinstance(self.unit, str) or not self.unit.strip():
            raise ValueError("Unit must be a non-empty string.")
        logger.info("Unit '%s' is valid.", self.unit)

    def validate_price(self):
        if not isinstance(self.price_per_unit, (int, float)) or self.price_per_unit <= 0:
            raise ValueError("Price per unit must be a positive number.")
        logger.info("Price per unit %s is valid.", self.price_per_unit)

    def validate_quantity(self):
        if not isinstance(self.available_quantity, (int, float)) or self.available_quantity < 0:
            raise ValueError("Available quantity must be a non-negative number.")
        logger.info("Available quantity %s is valid.", self.available_quantity)

    def display_info(self):
        return (
            f"Product: {self.name}, Unit: {self.unit}, Price/Unit: {self.price_per_unit}, "
            f"Available: {self.available_quantity} {self.unit}"
        )


