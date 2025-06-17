from fastapi import APIRouter
from core.models import Order
from utils.helper import generate_order_id
from qr_system.qr import generate_qr
from database.fake_db import fake_products

router = APIRouter()

@router.post("/order/create")
def create_order(product_id: int, to_base_id: int, user_id: int):
    product = next((p for p in fake_products if p.id == product_id), None)
    if not product:
        return {"error": "Mahsulot topilmadi"}
    
    order_id = generate_order_id()
    order = Order(
        id=order_id,
        product_id=product_id,
        from_base_id=product.base_id,
        to_base_id=to_base_id,
        user_id=user_id,
        status="pending"
    )
    
    payment_url = f"https://payme.uz/pay?amount={product.price}&order_id={order_id}"
    qr_code = generate_qr(payment_url)

    return {
        "order_id": order.id,
        "product": product.name,
        "from_base": product.base_id,
        "to_base": to_base_id,
        "price": product.price,
        "qr_code": qr_code
    }