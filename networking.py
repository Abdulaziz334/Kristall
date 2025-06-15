import socket

class NetworkEngine:
    def __init__(self):
        self.server_ip = "127.0.0.1"
        self.port = 8080

    def connect(self):
        print(f"Ulanmoqda: {self.server_ip}:{self.port}")