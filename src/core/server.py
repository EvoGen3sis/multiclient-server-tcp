import socket as socket

addr = ("127.0.0.1", 2119)

echo_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
echo_sock.bind(addr)
echo_sock.listen()

while True:
    cli_sock, cli_addr = echo_sock.accept()
    data = cli_sock.recv(1024)
    cli_sock.send(data)
    cli_sock.close()
