import sys
from fastapi import FastAPI,Query
from src.models.datamodels import Payload, Fuel
from typing import Annotated
from src.services.fuel_price_service import get_or_fetch_fuel_price

sys.stdout.reconfigure(encoding='utf-8')


app = FastAPI()

@app.get('/', response_model=Fuel)
async def get_fuel_price(payload:Annotated[Payload,Query()]) -> Fuel:
    return get_or_fetch_fuel_price(payload)

