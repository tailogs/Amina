import os
from datetime import datetime
import socket
from threading import Thread
from colorama import *
from hacker import portScanner
from utils import cursorPosition
from chat import chatClient, chatServer
from guiInterface import Gui
from games import Games

__dir__ = "User\\"
__cd__ = ""
__games__ = "Games\\"

init(autoreset = True)

def scanner(command=""):
    global __dir__, __cd__
    if command == "":
        command = input("\n>>> ").lower()
    if command == "help":
        print("Команды для управления системой:")
        print(Fore.BLUE + "HELP" + Fore.WHITE + " - Список всех команд")
        print(Fore.BLUE + "EXIT" + Fore.WHITE + " - Выключение системы")
        print(Fore.BLUE + "PRINT" + Fore.WHITE + " - Вывод текста после команды")
        print(Fore.BLUE + "CLS or CLEAR" + Fore.WHITE + " - Очистка консоли")
        print(Fore.BLUE + "SYSTEMINFO" + Fore.WHITE + " - Информация о системе")
        print(Fore.BLUE + "CF <FILE_NAME>" + Fore.WHITE + " - Создание файла")
        print(Fore.BLUE + "RENAME <FILE_NAME> <NEW_FILE_NAME>" + Fore.WHITE + " - Переименование файла")
        print(Fore.BLUE + "DEL <FILE_NAME>" + Fore.WHITE + " - Удаление файла")
        print(Fore.BLUE + "CAT <FILE_NAME>" + Fore.WHITE + " - Вывод содержимого файла")
        print(Fore.BLUE + "INSERT <FILE_NAME>" + Fore.WHITE + " - Вставка текста в файл")
        print(Fore.BLUE + "REPLACE <FILE_NAME>" + Fore.WHITE + " - Замена текста в файле")
        # Замена символов в файле
        print(Fore.BLUE + "MKDIR or MD" + Fore.WHITE + " - Создание папки")
        print(Fore.BLUE + "RMDIR or RD" + Fore.WHITE + " - Удаление папки")
        print(Fore.BLUE + "DIR or LS" + Fore.WHITE + " - Вывод содержимого директории")
        print(Fore.BLUE + "CD <FOLDER>" + Fore.WHITE + " - Переход в выбранную директорию")
        print(Fore.BLUE + "CD .." + Fore.WHITE + " - Переход на уровень выше")
        print(Fore.BLUE + "CD ." + Fore.WHITE + " - Переход в домашнюю директорию")
        print(Fore.BLUE + "DATETIME" + Fore.WHITE + " - Получение даты и времени")
        print(Fore.BLUE + "PORTSCANNER" + Fore.WHITE + " - Сканер портов: portScanner ip <number_of_ports>")
        print(Fore.BLUE + "CP" + Fore.WHITE + " - Отображение позиции курсора и цвета пикселя под ним")
        print(Fore.BLUE + "chatServer" + Fore.WHITE + " - Запуск сервера чата и отображение информации о сервере")
        print(Fore.BLUE + "chatClient" + Fore.WHITE + " - Запуск клиента чата и подключение к серверу")
        print(Fore.BLUE + "games" + Fore.WHITE + " - Включение режима игры и отображение списка доступных игр")
    elif command == "exit":
        print("[ Выход ]")
        exit()
    elif command.find("print") != -1:
        command = command.replace("print", "")
        print(Fore.YELLOW + command.strip())
    elif ((command == "cls") or (command == "clear")):
        cls_clear(100)
    elif command == "systeminfo":
        print(Fore.GREEN + "Система основана на языке программирования Python")
    elif command.find("cf") != -1:
        name_file = command.replace("cf", "")
        name_file_strip = name_file.strip()
        f_ = __dir__ + name_file_strip
        try:
            with open(f_, "w") as f:
                print(Fore.GREEN + "[ Файл " + name_file_strip + " создан ]")
        except Exception:
            print(Fore.GREEN + "[ Ошибка ] - Вы не указали имя файла")
    elif command.find("rename") != -1:
        f_ = command.split(" ")
        try:
            f_old = __dir__ + f_[1]
            f_new = __dir__ + f_[2]
            os.rename(f_old, f_new)
            print(Fore.GREEN + "[ Файл был переименован с " + f_old.replace(__dir__, "") + " на " + f_new.replace(__dir__, "") + " ]")
        except Exception:
            print(Fore.GREEN + "[ Ошибка ] - Пока система не может переименовывать файлы с пробелами в названии")
            print(Fore.GREEN + "[ Ошибка ] - Или вы не указали имя файла")
    elif command.find("del") != -1:
        f_ = command.split(" ")
        try:
            f_del = __dir__ + f_[1]
            os.remove(f_del)
            print(Fore.GREEN + "[ Файл " + f_[1] + " удален ]")
        except Exception:
            print(Fore.GREEN + "[ Ошибка ] - Пока система не может удалять файлы с пробелами в названии")
            print(Fore.GREEN + "[ Ошибка ] - Или вы не указали имя файла")
    elif command.find("cat") != -1:
        f_ = command.split(" ")
        try:
            f_cat = __dir__ + f_[1]
            print(Fore.GREEN + "[ Содержимое файла " + f_[1] + " ]")
            with open(f_cat, "r") as f:
                print(f.read())
        except Exception:
            print(Fore.GREEN + "[ Ошибка ] - Пока система не может удалять файлы с пробелами в названии")
            print(Fore.GREEN + "[ Ошибка ] - Или вы не указали имя файла")
    elif command.find("insert") != -1:
        f_ = command.split(" ")
        try:
            f_ins = __dir__ + f_[1]
            cls_clear(100)
            print(Fore.GREEN + "[ Если в имени файла был пробел, будет создан новый файл с именем до пробела. Я знаю об этой проблеме, но пока не решил ее. ]")
            print(Fore.GREEN + "[ Я установил ограничение в 10 000 строк, поэтому при достижении лимита сохраните файл и откройте его снова, иначе возможна потеря данных! ]")
            print(Fore.GREEN + "[ Чтобы сохранить и выйти, введите \"[save]\" без кавычек на отдельной строке ]")
            print(Fore.GREEN + "[ Чтобы выйти без сохранения, введите \"[exit]\" без кавычек на отдельной строке ]")
            cls_clear(3)
            with open(f_ins, "a") as f:
                text = ""
                for i in range(10000):
                    temp_ = input()
                    if temp_.lower() == "[save]":
                        d, t = dateAndTime()
                        f.write(f"\n\n\nДата: {d} \nВремя: {t} \n{text}")
                        print(Fore.GREEN + "[ Файл был обновлен ]")
                        break
                    elif temp_.lower() == "[exit]":
                        print(Fore.RED + "[ Изменения не сохранены ]")
                        break
                    else:
                        text += temp_ + "\n"
        except Exception:
            print(Fore.GREEN + "[ Ошибка ] - Вы не указали имя файла")
    elif command.find("replace") != -1:
        f_ = command.split(" ")
        try:
            f_ins = __dir__ + f_[1]
            cls_clear(100)
            print(Fore.GREEN + "[ Если в имени файла был пробел, будет создан новый файл с именем до пробела. Я знаю об этой проблеме, но пока не решил ее. ]")
            print(Fore.GREEN + "[ Я установил ограничение в 10 000 строк, поэтому при достижении лимита сохраните файл и откройте его снова, иначе возможна потеря данных! ]")
            print(Fore.GREEN + "[ Чтобы сохранить и выйти, введите \"[save]\" без кавычек на отдельной строке ]")
            print(Fore.GREEN + "[ Чтобы выйти без сохранения, введите \"[exit]\" без кавычек на отдельной строке ]")
            cls_clear(3)
            text = ""
            for i in range(10000):
                    temp_ = input()
                    if temp_.lower() == "[save]":
                        d, t = dateAndTime()
                        with open(f_ins, "w") as f:
                            f.write(f"Дата: {d} \nВремя: {t} \n{text}")
                        print(Fore.GREEN + "[ Файл был обновлен ]")
                        break
                    elif temp_.lower() == "[exit]":
                        print(Fore.RED + "[ Изменения не сохранены ]")
                        break
                    else:
                        text += temp_ + "\n"
        except Exception:
            print(Fore.GREEN + "[ Ошибка ] - Вы не указали имя файла")
    elif ((command.find("rmdir") != -1) or (command.find("rd") != -1)):
        d = command.split(" ")
        try:
            d_ = __dir__ + d[1]
            os.rmdir(d_)
            print(Fore.GREEN + "[ Каталог был удален ]")
        except Exception:
            print(Fore.GREEN + "[ Ошибка ] - Система не может читать файлы с пробелами в имени")
            print(Fore.GREEN + "[ Ошибка ] - Или вы не указали имя файла")
    elif ((command.find("mkdir") != -1) or (command.find("md") != -1)):
        d = command.split(" ")
        try:
            d_ = __dir__ + d[1]
            os.mkdir(d_)
            print(Fore.GREEN + "[ Каталог был создан ]")
        except Exception:
            print(Fore.GREEN + "[ Ошибка ] - Система не может читать файлы с пробелами в имени")
            print(Fore.GREEN + "[ Ошибка ] - Или вы не указали имя файла")
    elif ((command.find("ls") != -1) or (command.find("dir") != -1)):
        try:
            rez = sorted(os.listdir(__dir__))
            for n, item in enumerate(rez):
                #print(n+1, item)
                if item.find(".") != -1:
                    print("Файл:    ", item)
                else:
                    print("Папка: ", Fore.GREEN + item)
        except Exception:
            print(Fore.GREEN + "[ Ошибка ] - Такого каталога не существует, перейдите на уровень выше")
    elif command == "cd ..":
        __dir__ = __dir__.replace(__cd__, "")
        length = len(__cd__)
        print(Fore.GREEN + "[ Вы вышли из каталога " + __cd__[:length-1] + "и перешли на уровень выше ]")
        __cd__ = ""
    elif command == "cd .":
        __dir__ = "Пользователь\\"
    elif command.find("cd") != -1:
        try:
            cd_ = command.split(" ")
            __cd__ += cd_[1] + "\\"
            __dir__ += __cd__
            print(Fore.GREEN + "[ Вы перешли в каталог " + cd_[1] + " ]")
        except Exception:
            print(Fore.RED + "Вы не указали каталог!")
    elif command == "datetime":
        d, t = dateAndTime()
        print(Fore.CYAN + "Дата: " + d)
        print(Fore.CYAN + "Время: " + t)
    elif command.find("portscanner") != -1:
        try:
            start = datetime.now()
            ip = command.split(" ")
            if len(ip) == 3:
                if (int(ip[2]) > 65535) or (int(ip[2]) <= 0):
                    print(Fore.RED + "Порты указаны вне диапазона")
                else:
                    for i in range(int(ip[2])):
                        potoc = Thread(target=portScanner, args=(ip[1], i))
                        potoc.start()
            elif len(ip) == 2:
                for i in range(int(65535)):
                    potoc = Thread(target=portScanner, args=(ip[1], i))
                    potoc.start()
            else:
                pass
            ends = datetime.now()
            print(Fore.GREEN + "Время : {}".format(ends-start))
        except Exception:
            print(Fore.RED + "Вы не ввели IP-адрес!")
    elif command == "cp":
        print("Нажмите CTRL-C, чтобы выйти")
        try:
            while True:
                cursorPosition()
        # Когда пользователь нажимает CTRL-C, возникает исключение KeyboardInterrupt
        except KeyboardInterrupt:
            print("\nВыход из программы")
    elif command == "chatserver":
        chatServer()
    elif command.find("chatclient") != -1:
        try:
            IP = command.split(" ")
            chatClient(IP[1])
        except Exception:
            print(Fore.RED + "Вы не ввели IP-адрес!")
    elif command == "gui":
        try:
            pass
            #Gui()
        except Exception:
            pass
    elif command == "games":
        g = Games(__games__)
        g.startGameMode()
        print("\n[ Привет, Пользователь! ]")
    else:
        print(Fore.BLUE + "[ Команда не распознана ]")

def cls_clear(num):
    for i in range(num):
       print()

def dateAndTime():
    d = datetime.today().strftime("%d.%m.%Y")
    t = datetime.today().strftime("%H:%M:%S")
    return d, t