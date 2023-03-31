import socket
from _thread import *


ips = {}

conns = []

ip = "127.0.0.1"


def handler(conn, addr):
    
    flag = False
    
    with conn:

        while True:
        
            data = conn.recv(1024)

            if data.decode() == "reg":
                flag = True
                conn.sendall(bytes(">>>", encoding="utf-8"))
            else:
                if flag == True:
                    ips[addr] = data.decode()
                    flag = False
                    conn.sendall(b">>> ")
                else:
                    for i in conns:
                        if i[0] == addr:
                            i[1].sendall(b">>> ")
                        else:
                            print(f"{i[1]}")
                            i[1].sendall(bytes(ips[addr]+" >>> "+data.decode(), encoding="utf-8"))
                        


        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((ip, 8852))
    s.listen()

    while True:
        conn, addr = s.accept()

        conns.append([addr, conn])
        start_new_thread(handler, (conn, addr))
        print("New thread")

    