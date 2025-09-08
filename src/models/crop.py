import logging

logger = logging.getLogger(__name__)


class Crop:
    def __init__(self, name, variety=None, planting_date=None, expected_harvest_date=None):
        self.name = name
        self.variety = variety
        self.planting_date = planting_date  # 'YYYY-MM-DD' or None
        self.expected_harvest_date = expected_harvest_date  # 'YYYY-MM-DD' or None

        self.validate_name()
        self.validate_dates()

    def validate_name(self):
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("Crop name must be a non-empty string.")
        logger.info("Crop name '%s' is valid.", self.name)

    def _validate_date_str(self, date_str, field_name):
        from datetime import datetime
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            raise ValueError(f"{field_name} must be in 'YYYY-MM-DD' format.")

    def validate_dates(self):
        if self.planting_date:
            self._validate_date_str(self.planting_date, "Planting date")
            logger.info("Planting date %s is valid.", self.planting_date)
        if self.expected_harvest_date:
            self._validate_date_str(self.expected_harvest_date, "Expected harvest date")
            logger.info("Expected harvest date %s is valid.", self.expected_harvest_date)

    def display_info(self):
        parts = [f"Crop: {self.name}"]
        if self.variety:
            parts.append(f"Variety: {self.variety}")
        if self.planting_date:
            parts.append(f"Planted: {self.planting_date}")
        if self.expected_harvest_date:
            parts.append(f"Expected Harvest: {self.expected_harvest_date}")
        return ", ".join(parts)


