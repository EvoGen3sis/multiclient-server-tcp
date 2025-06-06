import socket
import threading
from datetime import datetime
import random
from client import Client
from message import Message

class Server:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 2119
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        #self.now = datetime().now()

    def gettime(self):
        now = datetime.now()
        now_str = now.strftime("%H:%M:%S")
        return now_str

    def client_accept(self):
        pass

    def broadcast(self, client_inst, data):
        for client in self.clients:
            if not client == client_inst:
                try:
                    client.conn.sendall(data)
                except:
                    self.client_remove(client)

    def client_remove(self, client_inst):
        if client_inst in self.clients:
            client_inst.conn.close()
            self.clients.remove(client_inst)
            mssg = "\n[!] {} has disconnected.".format(client_inst.username)
            print(mssg)

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

    def messageinst(self):
        pass

    def handle(self, client_inst):
        username = client_inst.conn.recv(1024).decode()
        client_inst.username = username
        print(f"\n[!] {username} connected.")
        try:
            while True:
                data = client_inst.conn.recv(1024)
                if not data:
                    break
                else:
                    #client_inst.conn.sendall(data)
                    self.broadcast(client_inst, data)
        finally:
            self.client_remove(client_inst)

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
                for clients in self.clients:
                    print(clients.username)
                threading.Thread(target = self.handle, args = (client_inst, ), daemon = True).start()
        except KeyboardInterrupt:
            print(f"\nShutting down...")
        finally:
            self.shutdown()

if __name__ == "__main__":
    server_inst = Server()
    server_inst.start()
