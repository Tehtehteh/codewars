import tornado.netutil
import tornado.tcpserver
import tornado.ioloop


class EchoServer(tornado.tcpserver.TCPServer):
    def handle_stream(self, stream, address):
        self.read_chunk_size()
