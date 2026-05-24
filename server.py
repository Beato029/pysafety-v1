import socket
import threading

class Server:    
    def __init__(self, host, port):
        super().__init__()

        self.host = host
        self.port = port

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = [] # [("conn0", 0), ("conn1", 1)]
        self.id = 0

        self.accept_connection_flag = False

    def config(self):
        self.server.bind((self.host, self.port))
        self.server.listen()

    def start_server(self):
        self.accept_connection_flag = True
        self.thread_accept = threading.Thread(target=self.accept_)
        self.thread_accept.start()

    def accept_(self):
        while self.accept_connection_flag:
            conn, addr = self.server.accept()
            self.clients.append((conn, self.id))
            self.id += 1

    def stop_server(self):
        self.accept_connection_flag = False
        self.server.close()
        self.thread_accept.join()




# client = []

# client.append(("client1", 0))