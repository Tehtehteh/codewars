import socket
import threading


def update(s, data, clients):
    while True:
        for client in clients:
            s.sendall(data)
            client.close()

def main():
    host, port = ('', 8888)
    clients = set()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(10)
    print('Serving @ ', host, port)
    #s.setblocking(0)
    while True:
        con, client = s.accept()
        clients.add(client)
        data = s.recv(1024)
        print('Received data {} from {}'.format(data, client))
        threading._start_new_thread(update, (s, data, clients))


main()