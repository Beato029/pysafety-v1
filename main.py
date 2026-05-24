from Core.alerts import *
from Core.colors import *
from Core.logo import *

logo()


class PySafety:
    def __init__(self):
        super().__init__()
        self.host = "1"
        self.port = "2"
        self.terminal()

    def terminal(self):
        while True:
            command = input("pysafety-console" + RED + "» " + RESET)

            if command == "exit":                
                break

            elif len(command.strip()) == 0:
                pass

            elif command.split()[0] == "server":
                command = command.split()
                match command[1]:
                    case "set":
                        match command[2]:
                            case "LHOST":
                                self.host = command[3]
                            case "LPORT":
                                self.port = command[3]
                                error(f"'{command[2]}' Parameter not found")
                        match command[4]:
                            case "LHOST":
                                self.host = command[5]
                            case "LPORT":
                                self.port = command[5]
                            case _:
                                error(f"'{command[4]}' Parameter not found")
                        
                    case "start":
                        True

                    case "show":
                        None
                    case _:
                        error(f"'{command[1]}' Parameter not found")

            elif command == "server star":
                "Server Start"

            else:
                error(f"'{command}' Command not found")


if __name__ == "__main__":
    pysafety = PySafety()