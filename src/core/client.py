import socket
import datetime
import time
import threading

class Client:
    def __init__(self, conn, addr, username: str, id: int):
        self.conn = conn
        self.addr = addr
        self.username = username
        self.id = id

    def send(self):
     pass

     def recv(self):
        pass

     def conn(self):
        pass
     
     def disconn(self):
        pass
