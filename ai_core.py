# ai_core.py

class AIEngine:
    def __init__(self):
        self.state = "idle"
        self.memory = {}
    
    def process_input(self, user_input):
        # Kiruvchi so‘rovni tahlil qilish
        if "move" in user_input:
            self.state = "moving"
        elif "stop" in user_input:
            self.state = "idle"
        else:
            self.state = "processing"
        return self.state

    def update_memory(self, key, value):
        self.memory[key] = value

    def get_memory(self, key):
        return self.memory.get(key, None)