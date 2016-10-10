import socket
import threading

host, port = '192.168.0.23', 8888
socketList = []
def update(socketList, add):
    while True:
        for conn in socketList:
            req = conn.recv(1024)
            conn.send('%s: %s' % (add,req))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(10)
print('Serving on %s %s' % (host, port))
while True:
    cc, ca = s.accept()
    socketList.append(cc)
    threading._start_new_thread(update, (socketList, ca))
    #cc.close()


# import logging
# from tornado.ioloop import IOLoop
# from tornado import gen
# from tornado.iostream import StreamClosedError
# from tornado.tcpserver import TCPServer
# from tornado.options import options, define

# define("port", default=8888, help="TCP port to listen on")
# logger = logging.getLogger(__name__)
#
#
# class EchoServer(TCPServer):
#     @gen.coroutine
#     def handle_stream(self, stream, address):
#         while True:
#             try:
#                 data = yield stream.read_until(b"\n")
#                 logger.info("Received bytes: %s", data, ' from address ', address[0])
#                 if not data.endswith(b"\n"):
#                     data = data + b"\n"
#                 yield stream.write(data)
#             except StreamClosedError:
#                 logger.warning("Lost client at host %s", address[0])
#                 break
#             except Exception as e:
#                 print(e)
#
#
# if __name__ == "__main__":
#     options.parse_command_line()
#     server = EchoServer()
#     server.listen(options.port)
#     logger.info("Listening on TCP port %d", options.port)
#     IOLoop.current().start()