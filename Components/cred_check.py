import socket
from Core.alerts import *

HOST = "localhost"
PORT = 8080

def try_address_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"Testing port: {str(port)}")
        sock.bind((host, int(port)))
        sock.close()
        success("Host & Port verified successfully ")
        return True
    except TypeError as e: # Inserito str() -> richiesto int()
        return error("Port must be int type (es. 5555)")
    except socket.gaierror as e: # Host invalido
        return error("")
    except OverflowError as e: # Porta troppo alta
        return error("Port must be 0 - 65535")
    except OSError as e:
        if e.errno == 98:
            return error("Port already in use, please change port")
    except Exception as e:
        return error(e) 


a = try_address_port(HOST, PORT)
print(a)