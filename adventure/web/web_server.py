import os
import socket

BIND_ADDR = "127.0.0.1"


def form_request(file, content_type):
    RESPONSE = """\
HTTP/1.1 200 OK
Content-type: text/{content}
Content-length: {len}

"""

    with open(os.path.abspath(file), encoding='utf-8') as text:
        text_str = text.read()
        text_bytes = bytearray(text_str, encoding='utf-8')
        response_bytes = bytearray(RESPONSE.format(len=len(text_bytes), content=content_type), encoding='utf-8').replace(b"\n", b"\r\n")
        return response_bytes + text_bytes


def request_file(file):
    with open(os.path.abspath(file), encoding='utf-8') as f:
        text = f.read()
    return bytearray(text, encoding='utf-8')


while True:
    with socket.socket() as sock:
        sock.bind((BIND_ADDR, 5000))
        sock.listen(0)
        client_sock, client_addr = sock.accept()
        client_data = client_sock.recv(1024)
        client_text = str(client_data, encoding='utf-8')

        client_list = client_text.split(" ")
        print(client_list)
        # Gets the string after "GET", and removes the "/"
        requested_file = client_list[1][1:]
        if not requested_file:
            requested_file = "adventure.html"
            content_type = "html"
        elif requested_file.endswith(".js"):
            content_type = "javascript"
        elif requested_file.endswith(".html"):
            content_type = "html"
        else:
            content_type = "text"
        print(requested_file, content_type)
        client_sock.sendall(form_request(requested_file, content_type))
