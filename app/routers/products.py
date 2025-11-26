from fastapi import APIRouter

router = APIRouter(prefix="/products")

products_data = [
    {"id": 1, "name": "T-Shirt", "price": 20},
    {"id": 2, "name": "Hoodie", "price": 40}
]

@router.get("/")
def get_all_products():
    return {"products": products_data}