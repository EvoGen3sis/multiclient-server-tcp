import socket
import threading

host, port = "127.0.0.1", 2119

def recieve(conn):
    try:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
    finally:
        conn.close()

def connect():
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((host, port))
    username = input(f"\nPlease enter your username: ")
    conn.sendall(username.encode())
    threading.Thread(target = recieve, args = (conn,), daemon = True).start()
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
