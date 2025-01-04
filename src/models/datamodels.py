from pydantic import BaseModel
from typing import Optional
from enum import Enum

class FuelType(str, Enum):
    pt = 'petrol'
    ds = 'diesel'

class Payload(BaseModel):
    city: str
    fuel_type: Optional[FuelType] = FuelType.pt

class Fuel(Payload):
    fuel_price: float

