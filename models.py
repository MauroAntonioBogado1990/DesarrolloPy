from fastapi import FastAPI
from pydantic import BaseModel


#desarrollamos los modelos
class Item(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float
    tax: str 
    quantity: int
    company : str