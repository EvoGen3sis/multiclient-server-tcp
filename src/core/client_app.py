import socket

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