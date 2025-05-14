import socket as socket

addr = ("127.0.0.1", 2119)

echo_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Initialise server (tcp) socket.
echo_sock.bind(addr) # Bind socket to address tuple e.g. (host, port).
echo_sock.listen() # Listen for incoming requests on server socket.

try:
    while True:
        cli_sock, cli_addr = echo_sock.accept() # Accepts a connection, returns a new socket to talk to the client.
        # Client and server now communicate directly via this connected socket (cli_sock).
        try:
            while True:
                data = cli_sock.recv(1024)
    # The connected socket (cli_sock) receives up to 1024 bytes from the client.             
                if not data:
                    break
    # When you disconnect from the telnet client, the client socket returns b"" (0 bytes).
    # This then calls "if not data", breaking the infinite loop and calling the "finally" block
                else:
                    cli_sock.send(data)
        finally:
            print(f"Client socket closed.")
            cli_sock.close() # Closes the socket connected to the client (cli_sock).

except KeyboardInterrupt:
    print(f"\tShutting down server...") # Ctrl C is pressed, server begins to shut down.
                
finally:
    print(f"Server socket closed.") # Server listening socket closes, server shuts down.
    echo_sock.close()
