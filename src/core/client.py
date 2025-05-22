import socket

class Client:
   def __init__(self, conn, id):
      self.conn = conn #socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.host = "127.0.0.1"
      self.port = 2119
      self.username = None
      self.id = id

   def connect(self):
      self.conn.connect((self.host, self.port))
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
