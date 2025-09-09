from utils.data_handler import read_json, write_json

class MarketService:
    def __init__(self):
        self.market_prices_file = "data/market_prices.json"
        self._initialize_market_prices()

    def _initialize_market_prices(self):
        """Initialize market prices with sample data if file doesn't exist"""
        prices = read_json(self.market_prices_file)
        if not prices:
            sample_prices = {
                "Rice": 450.00,
                "Maize": 320.00,
                "Wheat": 380.00,
                "Cassava": 180.00,
                "Yam": 250.00,
                "Plantain": 200.00,
                "Tomato": 400.00,
                "Onion": 350.00,
                "Pepper": 500.00,
                "Beans": 280.00,
                "Groundnut": 600.00,
                "Soybean": 450.00,
                "Sorghum": 300.00,
                "Millet": 320.00,
                "Cocoa": 1200.00,
                "Coffee": 800.00,
                "Palm Oil": 400.00,
                "Coconut": 150.00
            }
            write_json(self.market_prices_file, sample_prices)

    def get_market_prices(self):
        """Get current market prices"""
        return read_json(self.market_prices_file)

    def get_crop_price(self, crop_type):
        """Get price for a specific crop"""
        prices = self.get_market_prices()
        return prices.get(crop_type, 0.0)

    def update_crop_price(self, crop_type, new_price):
        """Update price for a specific crop"""
        prices = self.get_market_prices()
        prices[crop_type] = new_price
        write_json(self.market_prices_file, prices)

    def add_new_crop(self, crop_type, price):
        """Add a new crop with its price"""
        prices = self.get_market_prices()
        prices[crop_type] = price
        write_json(self.market_prices_file, prices)