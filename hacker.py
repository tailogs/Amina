import socket
from colorama import *

init(autoreset = True)

def portScanner(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        connect = sock.connect((ip, port))
        print(Fore.YELLOW + "Порт :" + str(port) + " открыт.")
        sock.close()
    except Exception:
        pass