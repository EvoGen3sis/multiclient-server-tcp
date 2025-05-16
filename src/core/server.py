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

    def timer(func):
        def wrapper():
            t1 = time.time()
            target = func()
            t2 = time.time()
            diff = t2 - t1
            print(f"{diff:.2f}")
            return diff, target
        return wrapper

    def start():
        server.bind(host, port)
        server.listen()
        client_socket = server.accept()
        
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
