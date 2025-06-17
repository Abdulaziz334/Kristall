import qrcode
from io import BytesIO
import base64

def generate_qr(payment_url: str) -> str:
    qr = qrcode.make(payment_url)
    buffer = BytesIO()
    qr.save(buffer)
    img_base64 = base64.b64encode(buffer.getvalue()).decode()
    return f"data:image/png;base64,{img_base64}"