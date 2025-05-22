import socket
import datetime
import time
import threading

host, port = "127.0.0.1", 2119

class Client:
   def __init__(self):
      self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.id = id
      self.username = None

   def connect(self):
      self.conn.connect((host, port))
      self.username = input(f"\nPlease enter your username: ")
      self.conn.sendall(self.username)
      try:
         while True:
            data = input()
            if not data.lower() == "quit":
               break
            else:
               self.conn.sendall(data.encode())
      
      except KeyboardInterrupt:
         pass

      finally:
         self.conn.close()

