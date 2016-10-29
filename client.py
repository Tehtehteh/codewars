import socket
import threading


def sendmsg(s):
    while 1:
        data = input()
        s.send(bytes(data, encoding='utf-8'))


def updates(s):
    while 1:
        dataBack = s.recv(1024)
        if dataBack:
            print('%s:' % (dataBack,))


def main():
    s = socket.socket()
    s.connect(('127.0.0.1', 8888))
    while 1:
<<<<<<< HEAD
        data = input()
        s.sendall(bytes(data, encoding='utf-8'))
=======
        threading._start_new_thread(sendmsg, (s,))
>>>>>>> f7ba475ad225548053724d793b766a9fae668c3c
        threading._start_new_thread(updates, (s,))

if __name__=='__main__':
    main()