import socket

class Client:
   def __init__(self, conn, addr, id):
      self.conn = conn #socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.host = "127.0.0.1"
      self.port = 2119
      self.addr = addr
      self.username = None
      self.id = id
