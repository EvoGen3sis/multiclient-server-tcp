import socket
import threading
import datetime
import time

host, port = "127.0.0.1", 2119

class Server:
    def __init__(self, host: str = host, port: int = port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []

    def client_accept(self):
        pass

    def broadcast(self):
        pass

    def client_remove(self):
        pass

    def shutdown(self):
        print(f"Server is shutting down...")
        self.server.close()

    def start(self):
        self.server.bind((self.host, self.port))
        self.server.listen()
        client_socket = self.server.accept()
        
        try:
            while True:
                try:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                finally:
                    client_socket.close()
                    print(f"")
        except KeyboardInterrupt:
            print(f"")
        finally:
            server.close()
            print(f"")

    

server = Server()
