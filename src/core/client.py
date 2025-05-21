import socket
import datetime
import time
import threading

host, port = "127.0.0.1", 2119

class Client:
    def __init__(self, conn, addr, id: int, username = None):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = tuple(host, port)
        self.id = id
        self.username = username

    def send(self):
     pass

     def recv(self):
      pass

     def conn(self):
        pass
     
     def disconn(self):
        pass
