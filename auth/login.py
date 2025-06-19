import json
import hashlib
import os

CONFIG_FILE = "auth/config.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_password_hash():
    if not os.path.exists(CONFIG_FILE):
        raise FileNotFoundError("Parol fayli topilmadi.")
    
    with open(CONFIG_FILE, "r") as f:
        data = json.load(f)
        return data.get("ADMIN_PASSWORD_HASH")

def login(input_password):
    stored_hash = load_password_hash()
    return hash_password(input_password) == stored_hash