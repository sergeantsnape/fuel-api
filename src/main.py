from bs4 import BeautifulSoup
import requests
import sys
from fastapi import FastAPI, status, HTTPException, Query
from models.datamodels import Payload, Fuel
from typing import Annotated
from src.utils.scraper import scrape_fuel_price

sys.stdout.reconfigure(encoding='utf-8')


app = FastAPI()

@app.get('/', response_model=Fuel)
async def get_fuel_price(payload:Annotated[Payload,Query()]) -> Fuel:
    print(payload)
    return scrape_fuel_price(payload)

