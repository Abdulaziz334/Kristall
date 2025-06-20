from graphics_engine import GraphicsEngine
from audio_engine import AudioEngine
from ui_manager import UIManager

def main():
    graphics = GraphicsEngine()
    audio = AudioEngine()
    ui = UIManager()

    graphics.add_object("Logo.png")
    audio.play_sound("intro.wav")
    ui.show_main_menu()

    while True:
        choice = input("Tanlovni kiriting: ")
        ui.handle_input(choice)

if __name__ == "__main__":
    main()