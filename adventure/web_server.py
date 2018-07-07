import socket

BIND_ADDR = "127.0.0.1"
CONNECT_ADDR = "127.0.0.1"

with socket.socket() as sock:
    sock.bind((BIND_ADDR, 5000))
    while True:
        sock.listen(0)
        client_sock, client_addr = sock.accept()
        client_data = client_sock.recv(1024)
