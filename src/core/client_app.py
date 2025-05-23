import socket
import threading
from datetime import datetime
from message import Message

class ClientInst:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 2119
        self.username = input(f"\nPlease enter your username: ")

    def receive(self, conn):
        try:
            while True:
                data = conn.recv(1024).decode()
                now = datetime.now()
                mssg = Message(self.username, data, now)
                if not data:
                    break
                print(f"{mssg.format}")
        finally:
            conn.close()

    def connect(self):
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((self.host, self.port))
        username = input(f"\nPlease enter your username: ")
        print(f"username confirmed: @{username}")
        conn.sendall(username.encode())
        threading.Thread(target = self.receive, args = (conn,), daemon = True).start()
        try:
            while True:
                data = input()
                if data.lower() == "quit":
                    break
                else:
                    conn.sendall(data.encode())
        finally:
            conn.close()

if __name__ == "__main__":
    clientinst = ClientInst()
    clientinst.connect()
