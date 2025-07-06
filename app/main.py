from fastapi import FastAPI
from app.database.connection import db
from app.routes import auth_route, product_routes

app = FastAPI()

app.include_router(auth_route.router, tags=["Auth"])
app.include_router(product_routes.router, tags=["Products"])

"""@app.get("/")
async def root():
    collections = await db.list_collection_names()
    return {"message": "Connected to MongoDB", "collections": collections}"""
@app.get("/")
async def root ():
    return {"message" : "Welcome to E-commerce Backend! "}

