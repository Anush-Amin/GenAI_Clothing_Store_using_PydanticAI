from fastapi import APIRouter
from ..models import Order
from ..database import orders_collection

router  = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("")
def place_order(order: Order):
    """
    APlace a new order for a user
    """
    order_data = order.model_dump()
    orders_collection.insert_one(order_data)
    return {"message": "Order placed successfully!"}