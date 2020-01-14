import socketserver

class Server(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            b = self.request.recv(1024)
            if not b:
                return
            self.request.sendall(b)

if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    srv = socketserver.TCPServer(("localhost", 8001), Server)
    srv.serve_forever()
