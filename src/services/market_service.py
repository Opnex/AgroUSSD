from src.utils.data_handler import read_json, write_json
import datetime

MARKET_PRICES_FILE = "data/market_prices.json"

class MarketService:
    def __init__(self):
        self.market_prices = self.load_prices()

    def load_prices(self):
        return read_json(MARKET_PRICES_FILE)

    def save_prices(self):
        write_json(MARKET_PRICES_FILE, self.market_prices)

    def get_current_price(self, product_name, location):
        """
        Return the latest price for a product at a specific location.
        """
        location_data = self.market_prices.get(location, {})
        product_prices = location_data.get(product_name, [])
        if not product_prices:
            return None  # No data

        # Assuming prices stored as list of dict with 'date' and 'price'
        latest_record = max(product_prices, key=lambda x: x["date"])
        return latest_record["price"]

    def compare_prices(self, product_name):
        """
        Compare prices for a product across all locations.
        Returns dict with location: latest_price.
        """
        comparison = {}
        for location, products in self.market_prices.items():
            prices = products.get(product_name, [])
            if prices:
                latest = max(prices, key=lambda x: x["date"])
                comparison[location] = latest["price"]
        return comparison

    def get_historical_trends(self, product_name, location, days=7):
        """
        Return price trend data for product and location for last 'days' days.
        """
        location_data = self.market_prices.get(location, {})
        product_prices = location_data.get(product_name, [])

        # Filter prices for last 'days'
        cutoff = (datetime.datetime.now() - datetime.timedelta(days=days)).strftime("%Y-%m-%d")
        filtered = [p for p in product_prices if p["date"] >= cutoff]
        # Sort by date ascending
        filtered.sort(key=lambda x: x["date"])

        return filtered

    def add_price_record(self, product_name, location, price, date=None):
        """
        Add a new price record for a product at a location.
        Date format YYYY-MM-DD. Defaults to today.
        """
        if not date:
            date = datetime.datetime.now().strftime("%Y-%m-%d")

        if location not in self.market_prices:
            self.market_prices[location] = {}
        if product_name not in self.market_prices[location]:
            self.market_prices[location][product_name] = []

        self.market_prices[location][product_name].append({
            "date": date,
            "price": price
        })
        self.save_prices()