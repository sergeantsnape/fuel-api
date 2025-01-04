from src.utils.cache import Cache
from src.utils.scraper import scrape_fuel_price
from src.models.datamodels import Payload, Fuel
import time

cache = Cache()

def get_or_fetch_fuel_price(payload: Payload) -> Fuel:
    t=time.time()
    key = f"fuel_price_{payload.city}_{payload.fuel_type}"
    cached_data = cache.get(key)

    if cached_data:
        return Fuel(city=payload.city,fuel_type=payload.fuel_type,fuel_price=cached_data)
    else:
        fuel_cost = scrape_fuel_price(payload)
        cache.set(key,fuel_cost.fuel_price)
        return fuel_cost