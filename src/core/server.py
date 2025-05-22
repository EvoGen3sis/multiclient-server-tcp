import socket
import threading
import datetime
import random
from client import Client

class Server:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 2119
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []

    def client_accept(self):
        pass

    def broadcast(self):
        for i in self.clients:
            pass

    def client_remove(self):
        pass

    def shutdown(self): # This method is liable to change
        messages = ["Server has shut down gracefully, byeee d[-_-]b",
                    "Server is going to sleep now... (￣ー￣) zzZ zzZ",
                    "Cleaning up connections... all done! (⌒‿⌒)",
                    "Emergency shutdown initiated! (╯°□°）╯",
                    "Server has shut down... see you next time. =^.^=",
                    "Server out. Catch you later! (⌐■_■)"]
        
        self.server.close()
        rand_message = random.choice(list(messages))
        print(f"\n{rand_message}")

    def handle(self, client_inst):
        username = client_inst.conn.recv(1024).decode()
        client_inst.username = username
        print(f"\n[!] {username} connected. ")
        try:
            while True:
                data = client_inst.conn.recv(1024)
                if not data:
                    break
                else:
                    client_inst.conn.sendall(data)
        finally:
            client_inst.conn.close()

    def start(self):
        self.server.bind((self.host, self.port))
        self.server.listen()
        print(f"Starting server...")
        try:
            while True:
                conn, addr = self.server.accept()
                id = len(self.clients) + 1
                client_inst = Client(conn, addr, id)
                self.clients.append(client_inst)
                threading.Thread(target = self.handle, args = (client_inst, ), daemon = True).start()
        except KeyboardInterrupt:
            print(f"\nShutting down...")
        finally:
            self.shutdown()

server_inst = Server()
server_inst.start()
