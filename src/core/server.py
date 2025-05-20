import socket
import threading
import datetime
import time
import random
from concurrent.futures import ThreadPoolExecutor
from client import Client


host, port = "127.0.0.1", 2119

class Server:
    def __init__(self, host: str = host, port: int = port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.pool = ThreadPoolExecutor(4)

    def client_accept(self):
        pass

    def broadcast(self):
        pass

    def client_remove(self):
        pass

    def shutdown(self): # This method is liable to change
        messages = ["Server has shut down gracefully, byeee (＾▽＾)/",
                    "Server is going to sleep now... (￣ー￣) zzZ zzZ",
                    "Cleaning up connections... all done! (⌒‿⌒)",
                    "Emergency shutdown initiated! (╯°□°）╯",
                    "Server has shut down... see you next time. (ノ﹏ヽ)",
                    "Server out. Catch you later! (⌐■_■)"]
        
        self.server.close()
        rand_message = random.choice(list(messages))
        print(f"\n{rand_message}")

    def handle(self, client_socket, client_addr):
        try:
            while True:
                client_inst = Client(client_socket, client_addr)
                data = client_inst.client_socket.recv(1024)
                if not data:
                    break
                else:
                    client_inst.client_socket.send(data)
        finally:
            client_inst.client_socket.close()

    def start(self):
        self.server.bind((self.host, self.port))
        self.server.listen(4)
        print(f"Starting...")
        try:
            while True:
                client_socket, client_addr = self.server.accept()
                self.pool.submit(self.handle, client_socket, client_addr)
        except KeyboardInterrupt:
            print(f"")
        finally:
            self.pool.shutdown(wait = True)
            self.shutdown()
            print(f"")

server = Server()
server.start()
#print(server.shutdown())
