import socket as socket

addr = ("127.0.0.1", 2119)

echo_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
echo_sock.bind(addr)
echo_sock.listen()

try:
    while True:
        cli_sock, cli_addr = echo_sock.accept()

        try:
            while True:
                data = cli_sock.recv(1024)
                
                if not data:
                    break
                else:
                    cli_sock.send(data)
        finally:
            print(f"Client socket closed.")
            cli_sock.close()

except KeyboardInterrupt:
    print(f"\tShutting down server...")
                
finally:
    print(f"Server socket closed.")
    echo_sock.close()
