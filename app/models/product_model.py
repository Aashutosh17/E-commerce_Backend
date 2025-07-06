from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    name : str = Field(..., min_length=2, max_length= 50)
    description :  Optional[str] = None
    price : float = Field(..., gt=0)
    in_stock : bool = True




