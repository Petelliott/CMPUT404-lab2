import socketserver
import socket
from multiprocessing import Process


def copy_sock(src, dest):
    def thread():
        while True:
            b = src.recv(1024)
            if not b:
                break
            dest.sendall(b)

        dest.shutdown(socket.SHUT_WR)

    p = Process(target=thread)
    p.start()
    return p

class Server(socketserver.BaseRequestHandler):
    def handle(self):
        host = "www.google.com"
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, 80))

        t1 = copy_sock(sock, self.request)
        t2 = copy_sock(self.request, sock)

        t1.join()
        t2.join()

        sock.close()

if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    srv = socketserver.TCPServer(("localhost", 8001), Server)
    srv.serve_forever()
