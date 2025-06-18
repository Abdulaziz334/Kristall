import uuid
import json
import os
from datetime import datetime

PAYMENTS_FILE = "payment_module/payments.json"

def process_payment(order_id, amount, method, payer_id):
    payment = {
        "payment_id": str(uuid.uuid4()),
        "order_id": order_id,
        "payer_id": payer_id,
        "amount": amount,
        "method": method,  # QR-PAYME / QR-CLICK / UZC
        "status": "success",  # Hozircha oddiy qilish
        "timestamp": datetime.utcnow().isoformat()
    }

    save_payment(payment)
    update_order_status(order_id, "paid")
    return payment

def save_payment(payment):
    if not os.path.exists(PAYMENTS_FILE):
        with open(PAYMENTS_FILE, "w") as f:
            json.dump([], f)
    
    with open(PAYMENTS_FILE, "r+") as f:
        data = json.load(f)
        data.append(payment)
        f.seek(0)
        json.dump(data, f, indent=4)

def update_order_status(order_id, new_status):
    from order_module.order import ORDERS_FILE

    with open(ORDERS_FILE, "r+") as f:
        orders = json.load(f)
        for o in orders:
            if o["order_id"] == order_id:
                o["status"] = new_status
                break
        f.seek(0)
        f.truncate()
        json.dump(orders, f, indent=4)