from bs4 import BeautifulSoup
import requests
from src.models.datamodels import Payload, Fuel
from src.models.errors import (
    ExternalSourceError, CityNotFoundError,
    PriceNotFoundError, UnexpectedError)

URL = "https://www.livemint.com/fuel-prices"

def scrape_fuel_price(payload: Payload) -> Fuel:
    query_url = f"{URL}/{payload.fuel_type.lower()}-city-{payload.city.lower()}"

    try:
        response = requests.get(query_url)

        if response.status_code != 200:
            raise ExternalSourceError()
        
        # create BeautifulSoup instance
        soup = BeautifulSoup(response.text,'lxml')

        # extract city data
        city_data = soup.find('div',class_='fuelPrice')
        if city_data is None:
            raise CityNotFoundError(city=payload.city)
        
        try:
            fuel_price_str = city_data.find('div', class_=['up', 'down']).contents[0]
            fuel_price = float(fuel_price_str[1:])
            return Fuel(city=payload.city,fuel_type=payload.fuel_type,fuel_price=fuel_price)
        
        except Exception as ex:
            raise PriceNotFoundError(
                    city=payload.city,
                    fuel=payload.fuel_type
                ) from ex
        
    except (ExternalSourceError, CityNotFoundError, PriceNotFoundError) as e:
        raise e
    
    except Exception as ex:
        raise UnexpectedError()