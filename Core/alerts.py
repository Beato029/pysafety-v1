from Core.colors import *
from datetime import datetime


def get_time():
    return datetime.now().strftime("%H:%M:%S") + " "

def warning(text):
    print(YELLOW + "[/]" + get_time() + " Warning: " + text + RESET)

def error(text):
    print(RED + "[-] " + get_time() + " Error: " + text + RESET)

def success(text):
    print(GREEN + "[+] " + get_time() + text + RESET)

def information(text):
    print(BLUE + "[*] " + get_time() + " " + text + RESET)


# warning("Ciao")
# error("Ciao")
# success("Ciao")
# information("Ciao")