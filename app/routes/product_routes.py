from http.client import HTTPException

from bson import ObjectId
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

@router.get("/Products/Product_id")
async def get_product_by_id(product_id: str):
    if not ObjectId.is_valid(product_id):
        raise HTTPException(status_code = 400, detail = "Invalid ID Format!")

    product = await db["prodcuts"].find_one({"_id": ObjectId(product_id)})

    if not product:
        raise HTTPException(status_code = 404, detail= "Product not found!")

    product ['_id'] = str(product['_id'])
    return product


