class UIManager:
    def __init__(self):
        self.elements = []

    def add_button(self, name):
        self.elements.append(f"Button: {name}")
        print(f"Tugma qo‘shildi: {name}")
# ui_manager.py

class UIManager:
    def __init__(self):
        self.current_screen = "main_menu"

    def show_main_menu(self):
        print("\n🧠 KristallEngine Bosh Menyusi")
        print("1. O'yinni boshlash")
        print("2. Sozlamalar")
        print("3. Dvijok haqida")
        print("4. Chiqish")

    def show_settings(self):
        print("\n⚙️ Sozlamalar:")
        print("1. Ekran o'lchami")
        print("2. Ovoz")
        print("3. Tilda o'zgartirish")
        print("4. Orqaga")

    def show_about(self):
        print("\nℹ️ KristallEngine — AI asosida ishlovchi, Python’da yozilgan, Unreal+Unity uslubidagi o‘yin dvijogi.")

    def handle_input(self, choice):
        if self.current_screen == "main_menu":
            if choice == "1":
                print("▶️ O'yin boshlanyapti...")
            elif choice == "2":
                self.current_screen = "settings"
                self.show_settings()
            elif choice == "3":
                self.show_about()
            elif choice