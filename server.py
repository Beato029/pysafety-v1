import socket

class Server:
    def __init__(self, host, port):
        super().__init__()

        self.host = host
        self.port = port

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = [] # [("client0", 0), ("client1", 1)]
        

    def config(self):
        self.server.bind((self.host, self.port))
        

client = []

client.append(("client1", 0))