from graphics_engine import GraphicsEngine
from audio_engine import AudioEngine
from ui_manager import UIManager
from ai_core import AIEngine
from physics_core import PhysicsEngine
from scene_manager import SceneManager

# Modul obyektlari
graphics = GraphicsEngine()
audio = AudioEngine()
ui = UIManager()
ai = AIEngine()
physics = PhysicsEngine()
scene = SceneManager()

# Test
scene.create_scene("menu")
ui.add_button("Start")
graphics.add_object("Logo.png")
audio.play_sound("intro.wav")
print(ai.process_input("move"))
print("Gravitatsiya:", physics.apply_gravity(1, 5))
# main.py

from ui_manager import UIManager

def main():
    ui = UIManager()
    ui.show_main_menu()

    while True:
        user_input = input("Tanlovni kiriting: ")
        ui.handle_input(user_input)

if __name__ == "__main__":
    main()
from fastapi import FastAPI
from api.routes import router as api_router

app = FastAPI(title="Kristallengine")

app.include_router(api_router)
from fastapi import FastAPI
from api import order

app = FastAPI(title="Kristallengine API")

app.include_router(order.router, prefix="/api")
from auth.login import login

parol = input("🔐 KristallEngine’ga kirish uchun parolni kiriting: ")

if login(parol):
    print("✅ Kirish muvaffaqiyatli. KristallEngine ishga tushmoqda...")
    # Asosiy tizimni bu yerga yozasiz
else:
    print("❌ Noto‘g‘ri parol. Kirish rad etildi.")
from order_module import create_order
from payment_module import process_payment
from ai_engine import log_user_action

# 1. Buyurtma yaratish
user_id = "user_456"
product_id = "prod789"
user_location = "Toshkent"

order = create_order(user_id, product_id, user_location)
print("Buyurtma:", order)

# 2. Foydalanuvchi harakatini yozish (AI kuzatuv uchun)
log_user_action(user_id, "created_order", {
    "order_id": order["order_id"],
    "product_id": product_id
})

# 3. To‘lovni amalga oshirish
payment = process_payment(
    order_id=order["order_id"],
    amount=120000,
    method="QR-PAYME",
    payer_id=user_id
)
print("To‘lov natijasi:", payment)