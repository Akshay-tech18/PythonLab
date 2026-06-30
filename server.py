import socket, threading

s = socket.socket()

s.bind(("127.0.0.1", 6000))
s.listen()

clients = []

def chat(c, addr):
    clients.append(c)
    print(f"{addr} joined")

    while True:
        try:
            msg = c.recv(1024)
            print(msg.decode())

            for i in clients:
                if i != c:
                    i.send(msg)

        except:
            print(f"{addr} left")
            clients.remove(c)
            break

print("Server Started")

while True:
    c, addr = s.accept()
    threading.Thread(target=chat, args=(c, addr)).start()