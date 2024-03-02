from textInterface import cls_clear
from colorama import *

init(autoreset = True)

def startSystem():
    cls_clear(100)
    print('----------------')
    print('[ ЗАПУСК СИСТЕМЫ ]')
    print('----------------')
    print(Fore.GREEN + '\n[ Система готова к работе ]')