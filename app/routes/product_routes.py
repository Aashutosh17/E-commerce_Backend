from fastapi import APIRouter
from app.models.product_model import Product
from app.database.connection import db

router = APIRouter()

@router.post("/Products")
async def add_Product(product:Product):
    prodcut_dict = product.model_dump()
    result = await db["product"].insert_one(prodcut_dict)
    return {"message": "Product added", "id": str(result.inserted_id)}

@router.get("/Products")
async def get_Products(product: Product):
    products = []
    async  for product in db["product"].find_one():
        product ["_id"] = str(product["id"])
        products.append(product)

    return products


