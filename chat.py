import socket
from colorama import *

PORT = 8080

def chatClient(IP):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP, PORT))
    flag = True
    while flag:
        client.send(input("Я: ").encode("utf-8"))
        msg = client.recv(1024).decode("utf-8")
        if msg == "quit":
            print(Fore.GREEN + "[ Завершение чата и программы ]")
            flag = False
        else:
            print(Fore.CYAN + "_: " + msg)
    client.close()

def chatServer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP = socket.gethostbyname(socket.gethostname())
    print("Адрес сервера: " + IP)   
    server.bind((IP, PORT))
    server.listen()
    client, address = server.accept()
    flag = True
    while flag:
        msg = client.recv(1024).decode("utf-8")
        if msg == "quit":
            print(Fore.GREEN + "[ Выключение сервера и завершение программы ]")
            flag = False
        else:
            print(Fore.CYAN + "_: " + msg)
        client.send(input("Сервер: ").encode("utf-8"))
    client.close()
    server.close()
