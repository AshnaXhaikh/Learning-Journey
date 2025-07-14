# from fastapi import APIRouter

# router = APIRouter(
#     prefix="/items",
#     tags=["items"]
# )

# items_db = {
#     1: {"name": "Apple", "price": 1.0},
#     2: {"name": "Banana", "price": 0.5},
#     3: {"name": "Orange", "price": 0.8},
# }

# @router.get("/")
# def list_items():
#     return items_db

# @router.get("/{item_id}")
# def get_item(item_id: int):
#     item = items_db.get(item_id)
#     if item:
#         return item
#     return {"error": "Item not found"}

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, List, Union

# 1. Create the APIRouter for Items
items_router = APIRouter()

# 2. In-memory storage for items
items_data: Dict[int, Dict] = {
    101: {"name": "Laptop", "price": 1200},
    102: {"name": "Headphones", "price": 150},
    103: {"name": "Mouse", "price": 30}
}

# 3. Pydantic model for new items
class Item(BaseModel):
    name: str
    price: Union[int, float]

# 4. CRUD routes
@items_router.get("/items/")
def list_items():
    return items_data

@items_router.get("/items/{item_id}")
def get_item(item_id: int):
    item = items_data.get(item_id)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

@items_router.post("/items/")
def create_item(item_id: int, item: Item):
    if item_id in items_data:
        raise HTTPException(status_code=400, detail="Item ID already exists")
    items_data[item_id] = item.dict()
    return {
    "message": "Item created successfully",
    "item": item_id,
    "name": item.name,
    "price": item.price
}


@items_router.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items_data:
        raise HTTPException(status_code=404, detail="Item not found")
    items_data[item_id] = item.dict()
    return {"message": "Item updated successfully", "item": items_data[item_id]}

@items_router.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items_data:
        raise HTTPException(status_code=404, detail="Item not found")
    deleted = items_data.pop(item_id)
    return {"message": "Item deleted successfully", "item": deleted}

