from pydantic import BaseModel
from typing import Optional

class Payload(BaseModel):
    city: str
    fuel_type: Optional[str] = 'petrol'

class Fuel(Payload):
    fuel_price: float

