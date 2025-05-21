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
        messages = ["Server has shut down gracefully, byeee d[-_-]b",
                    "Server is going to sleep now... (￣ー￣) zzZ zzZ",
                    "Cleaning up connections... all done! (⌒‿⌒)",
                    "Emergency shutdown initiated! (╯°□°）╯",
                    "Server has shut down... see you next time. =^.^=",
                    "Server out. Catch you later! (⌐■_■)"]
        
        self.server.close()
        rand_message = random.choice(list(messages))
        print(f"\n{rand_message}")

    def handle(self, conn, caddr):
        #client_inst = Client(conn, caddr)
        try:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                else:
                    conn.sendall(data)
        finally:
            conn.close()

    def start(self):
        self.server.bind((self.host, self.port))
        self.server.listen()
        print(f"Starting server...")
        try:
            while True:
                conn, caddr = self.server.accept()
                #self.pool.submit(self.handle, (conn, caddr))
                thread = threading.Thread(target = self.handle, args = (conn, caddr), daemon = True)
                thread.start()
        except KeyboardInterrupt:
            print(f"Shutting down...")
        finally:
            #self.pool.shutdown(wait = True)
            #thread.join()
            self.shutdown()

server = Server()
server.start()
