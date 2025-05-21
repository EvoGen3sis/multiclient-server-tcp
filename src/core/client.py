import socket
import datetime
import time
import threading

class Client:
    def __init__(self, conn, addr, id: int, username = None):
        self.conn = conn
        self.addr = addr
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
