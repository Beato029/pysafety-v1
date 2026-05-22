import socket

HOST = "localhost"
PORT = 8080

def try_address_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"Testing port: {str(port)}")
        sock.bind((host, port))
        sock.close()
        return True
    except TypeError as e: # Inserito str() -> richiesto int()
        return e.args
    except socket.gaierror as e: # Host invalido
        return e.args
    except OverflowError as e: # Porta troppo alta
        return e.args
    except OSError as e:
        # print(e.errno, e.strerror)
        if e.errno == 98:
            return "Error: Port already in use"
    except Exception as e:
        return e.args


a = try_address_port(HOST, PORT)
print(a)