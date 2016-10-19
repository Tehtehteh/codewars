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
    s.connect(('192.168.0.23', 8888))
    while 1:
        threading._start_new_thread(sendmsg, (s,))
        threading._start_new_thread(updates, (s,))

if __name__=='__main__':
    main()