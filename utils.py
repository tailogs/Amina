import time
from threading import Thread
import pyautogui
from colorama import Fore, Back, Style, just_fix_windows_console
from color import rgb_to_hex

just_fix_windows_console()

"""Function for working with the cursor"""
def cursorPosition():
    """The procedure for calculating the cursor position"""
    x, y = pyautogui.position() # Получение текущих координат
    positionStr = 'X:' + str(x).rjust(5) + ' Y:' + str(y).rjust(5) # Метод rjust(4) сдвигает строку на четыре позиции вправо
    pixelColor = pyautogui.screenshot().getpixel((x, y)) # Получаем цвет пикселя по координатам курсора
    colorStr = "RGB: (" + str(pixelColor[0]).rjust(3)
    colorStr += ", " + str(pixelColor[1]).rjust(3)
    colorStr += ", " + str(pixelColor[2]).rjust(3) + ")"
    hex = 'Hex: #' + rgb_to_hex(pixelColor[0], pixelColor[1], pixelColor[2])
    print(Fore.BLUE + positionStr + '  ' + Fore.GREEN + colorStr + ' ' + Fore.YELLOW + hex, end='') # end предотвращает добавление символа новой строки, без этого старые координаты удалить не получиться
    print('\b' * (3 + len(positionStr + colorStr + hex)), end='', flush=True) # escape-символ \b стирает конец строки и чтобы удалить всю строку умножаем его на длину строки  
    print(Style.RESET_ALL, end='')
    time.sleep(0.01) # Для предотвращения мигания при выполнении цикла используем засыпание