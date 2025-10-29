from pydantic import BaseModel
from datetime import date

class Expense(BaseModel):
    id: int
    description: str
    amount: float
    category: str
    date: date
