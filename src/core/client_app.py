import socket

host, port = "127.0.0.1", 2119

def connect():
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((host, port))
    username = input(f"\nPlease enter your username: ")
    conn.sendall(username.encode())
    try:
        while True:
            data = input()
            if data.lower() == "quit":
               break
            else:
               conn.sendall(data.encode())
    finally:
        conn.close()

if __name__ == "__main__":
    connect()
