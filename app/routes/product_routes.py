from bson import ObjectId
from fastapi import APIRouter, HTTPException, Depends
from app.models.product_model import Product
from app.database.connection import db
from app.core.jwt import decode_access_token

router = APIRouter()

# Add product
@router.post("/products")
async def add_product(product: Product, email: str = Depends(decode_access_token)):
    product_dict = product.model_dump()
    product_dict["created_by"] = email
    result = await db["products"].insert_one(product_dict)
    return {"message": "Product added", "id": str(result.inserted_id)}

# Get all products
@router.get("/products")
async def get_products():
    products = []
    async for product in db["products"].find():
        product["_id"] = str(product["_id"])
        products.append(product)
    return products

# Get product by ID
@router.get("/products/{product_id}")
async def get_product_by_id(product_id: str):
    if not ObjectId.is_valid(product_id):
        raise HTTPException(400, "Invalid ID format!")

    product = await db["products"].find_one({"_id": ObjectId(product_id)})

    if not product:
        raise HTTPException(404, "Product not found!")

    product["_id"] = str(product["_id"])
    return product

# Update product
@router.put("/products/{product_id}")
async def update_product(product_id: str, product_data: Product, email: str = Depends(decode_access_token)):

    if not ObjectId.is_valid(product_id):
        raise HTTPException(400, "Invalid ID format!")

    result = await db["products"].update_one(
        {"_id": ObjectId(product_id)},
        {"$set": product_data.model_dump()}
    )

    if result.modified_count == 0:
        raise HTTPException(404, "Product not found or no changes made!")

    return {"message": "Product updated successfully"}

# Delete product
@router.delete("/products/{product_id}")
async def delete_product(product_id:str, email: str = Depends(decode_access_token)):
    if not ObjectId.is_valid(product_id):
        raise HTTPException(400, "Invalid ID Format!")

    result = await db["products"].delete_one({"_id":ObjectId(product_id)})

    if result.deleted_count == 0:
        raise HTTPException(404, "Product not found!")

    return {"message":"Product deleted successfully!"}