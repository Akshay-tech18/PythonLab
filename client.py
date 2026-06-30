import socket, threading

c = socket.socket()
c.connect(("127.0.0.1", 6000))

name = input("Name: ")

def receive():
    while True:
        print(c.recv(1024).decode())

def send():
    while True:
        c.send(f"{name}: {input()}".encode())

threading.Thread(target=receive).start()
threading.Thread(target=send).start()