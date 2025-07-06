from fastapi import APIRouter
from app.models.product_model import Product
from app.database.connection import db

router = APIRouter()

@router.post("/Products")
async def add_Product(product:Product):
    prodcut_dict = product.model_dump()
    result = await db["Product"].insert_one(prodcut_dict)
    return {"message": "Product added", "id": str(result.inserted_id)}

