import socket

if __name__ == "__main__":
    host = "localhost"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, 8001))
    sock.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")
    sock.shutdown(socket.SHUT_WR)
    while True:
        b = sock.recv(4096)
        if len(b) == 0:
            break

        print(b.decode("ISO-8859-1"))
    sock.close()
