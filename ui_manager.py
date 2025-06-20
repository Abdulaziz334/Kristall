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
        print("3. Til")
        print("4. Orqaga")

    def show_about(self):
        print("\nℹ️ KristallEngine — AI asosida ishlovchi, Python’da yozilgan, Unreal+Unity uslubidagi o‘yin dvijogi.")

    def handle_input(self, choice):
        if self.current_screen == "main_menu":
            if choice == "1":
                print("▶️ O'yin boshlanyapti... (Hozircha o'yin dvijogi yo'q)")
            elif choice == "2":
                self.current_screen = "settings"
                self.show_settings()
            elif choice == "3":
                self.show_about()
                self.show_main_menu()
            elif choice == "4":
                print("🔚 Chiqish...")
                exit()
            else:
                print("❗ Noto‘g‘ri tanlov!")
                self.show_main_menu()

        elif self.current_screen == "settings":
            if choice == "1":
                print("📐 Ekran o‘lchami sozlanmoqda...")
            elif choice == "2":
                print("🔊 Ovoz sozlanmoqda...")
            elif choice == "3":
                print("🌐 Til sozlanmoqda...")
            elif choice == "4":
                self.current_screen = "main_menu"
                self.show_main_menu()
            else:
                print("❗ Noto‘g‘ri tanlov!")
                self.show_settings()


# Programmani ishga tushirish qismi:
if __name__ == "__main__":
    ui = UIManager()
    ui.show_main_menu()

    while True:
        user_choice = input("Tanlovingizni kiriting: ")
        ui.handle_input(user_choice)