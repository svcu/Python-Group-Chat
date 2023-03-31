import socket
from threading import Thread

def rec(socket):
    while True:
        data = socket.recv(3072)

        if data:
            print(f"{data.decode()}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 8852))
    s.sendall(b"reg")

    task = Thread(target=rec, args=[s])
    task.start()

    while True:
        
        send = input()
        s.sendall(bytes(send, encoding="utf-8"))
