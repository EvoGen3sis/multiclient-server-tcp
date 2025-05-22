import socket

host, port = "127.0.0.1", 2119

class Client:
   def __init__(self):
      self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.id = id
      self.username = None

   def connect(self):
      self.conn.connect((host, port))
      self.username = input(f"\nPlease enter your username: ")
      self.conn.sendall(self.username.encode())
      try:
         while True:
            data = input()
            if data.lower() == "quit":
               break
            else:
               self.conn.sendall(data.encode())
      finally:
         self.conn.close()
