from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    weight_kg: float
    price: float
    base_id: int  # Qaysi bazada joylashgani

class Order(BaseModel):
    id: int
    product_id: int
    from_base_id: int
    to_base_id: int
    user_id: int
    status: str  # pending, on_the_way, delivered