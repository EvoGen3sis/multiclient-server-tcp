import socket
import datetime
import time
import threading

host, port = "127.0.0.1", 2119

class Client:
   def __init__(self, conn, addr, id: int, username = None):
      self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.addr = addr
      self.id = id
      self.username = username

   def connect(self):
      self.conn.connect((host, port))
      self.username = input(f"\nPlease enter your username: ")

      try:
         while True:
            data = input(f"")
            if not data:
               break
            else:
               self.conn.sendall(data)
      
      except:
         pass

      finally:
         pass
         
   def disconn(self):
      pass
