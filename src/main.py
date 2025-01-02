from bs4 import BeautifulSoup
import requests
import sys
from fastapi import FastAPI, status, HTTPException, Query
from src.datamodels import Payload, Fuel
from typing import Annotated

sys.stdout.reconfigure(encoding='utf-8')


app = FastAPI()

@app.get('/', response_model=Fuel)
async def get_fuel_price(payload:Annotated[Payload,Query()]) -> Fuel:
    print(payload)
    try:
        url = f'https://www.livemint.com/fuel-prices/{payload.fuel_type.lower()}-city-{payload.city.lower()}'
        response = requests.get(url)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to fetch data from external source")
        
        # create BeatifulSoup instance
        soup = BeautifulSoup(response.text,'lxml')
        
        # extract city data
        city_data = soup.find('div', class_='fuelPrice')
        if city_data is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"City '{payload.city}' not found"
            )

        try:
            fuel_price_str = city_data.find('div', class_=['up', 'down']).contents[0]
            fuel_price = float(fuel_price_str[1:])
            return Fuel(city=payload.city,fuel_type=payload.fuel_type,fuel_price=fuel_price)
        
        except Exception as ex:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Could not find price details for '{payload.city}'"
            ) from ex
    
    except HTTPException as http_exc:
        raise http_exc
    
    except Exception as e:
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Unexpected Error"
            ) from e

