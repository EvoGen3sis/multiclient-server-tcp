import socket
import datetime
import time
import threading

class Client:
    def __init__(self, conn, addr, username, id, message):
        self.conn = conn
        self.addr = addr
        self.username = username
        self.id = id
        self.message = message

    def send(self):
     pass

     def recv(self):
        pass

     def conn(self):
        pass
     
     def disconn(self):
        pass
