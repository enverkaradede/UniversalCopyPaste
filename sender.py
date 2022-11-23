import socket
import pyperclip

HOST = '127.0.0.1'
PORT = 12345

def SendCopiedTextToServer(text):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(bytes(text, encoding='cp1254'))
    pyperclip.copy('')
    data = s.recv(1024)

    print(f'Received data {data}')
