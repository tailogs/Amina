import sys
import time
import os
from colorama import init, Fore

init(autoreset=True)

def clear_console():
    # Очистка консоли
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

init(autoreset=True)

def draw_pet(name, happiness, sadness):
    # Отрисовка виртуального питомца с учетом счастья, грусти и имени
    print(Fore.BLUE + " /\\_/\\ ")
    print(Fore.BLUE + "( o.o )")
    print(Fore.BLUE + " > ^ <" + Fore.RESET)

def play(name, happiness, sadness):
    print(Fore.YELLOW + f"Вы играете с {name}!" + Fore.RESET)
    # Ваша логика игры с виртуальным питомцем
    happiness += 1
    sadness -= 1
    return happiness, sadness

def feed(name, happiness, sadness):
    print(Fore.MAGENTA + f"Вы кормите {name}!" + Fore.RESET)
    # Ваша логика кормления виртуального питомца
    happiness += 1
    sadness -= 1
    return happiness, sadness

def sleep(name, happiness, sadness):
    print(Fore.CYAN + f"{name} засыпает..." + Fore.RESET)
    # Ваша логика сна виртуального питомца
    happiness -= 1
    sadness += 1
    return happiness, sadness

def show_menu(name, happiness, sadness):
    print("1. " + Fore.GREEN + "Играть")
    print("2. " + Fore.YELLOW + "Кормить")
    print("3. " + Fore.MAGENTA + "Уложить спать")
    print("4. " + Fore.RED + "Выход")
    print("Имя: {}".format(Fore.GREEN + name + Fore.RESET))  # Окрашиваем имя в зеленый цвет
    print("Счастье: {}".format(Fore.YELLOW + str(happiness) + Fore.RESET))  # Окрашиваем уровень счастья в желтый цвет
    print("Грусть: {}".format(Fore.RED + str(sadness) + Fore.RESET))  # Окрашиваем уровень грусти в красный цвет

def save_data(name, happiness, sadness):
    # Сохранение данных в файл
    script_path = os.path.dirname(__file__)
    with open(script_path + "\\data\\pet_data.txt", "w") as file:
        file.write(f"{name},{happiness},{sadness}")

def load_data():
    # Чтение данных из файла
    script_path = os.path.dirname(__file__)
    try:
        with open(script_path + "\\data\\pet_data.txt", "r") as file:
            data = file.readline().strip().split(",")
            name = data[0]
            happiness = int(data[1])
            sadness = int(data[2])
            return name, happiness, sadness
    except FileNotFoundError:
        # Если файл не найден, возвращаем значения по умолчанию
        return None, 5, 5

def main():
    #clear_console()

    # Загрузка данных из файла
    pet_name, pet_happiness, pet_sadness = load_data()

    if pet_name is None:
        pet_name = input("Введите имя для вашего виртуального питомца: ")
    
    is_running = True

    while is_running:
        #clear_console()
        draw_pet(pet_name, pet_happiness, pet_sadness)
        show_menu(pet_name, pet_happiness, pet_sadness)

        choice = input("Выберите действие: ")

        if choice == "1":
            pet_happiness, pet_sadness = play(pet_name, pet_happiness, pet_sadness)
        elif choice == "2":
            pet_happiness, pet_sadness = feed(pet_name, pet_happiness, pet_sadness)
        elif choice == "3":
            pet_happiness, pet_sadness = sleep(pet_name, pet_happiness, pet_sadness)
        elif choice == "4":
            is_running = False
        else:
            print("Неправильный выбор. Попробуйте еще раз.")

        # Ограничение счастья и грусти в диапазоне от 0 до 10
        pet_happiness = max(0, min(pet_happiness, 10))
        pet_sadness = max(0, min(pet_sadness, 10))

        # Сохранение данных в файл
        save_data(pet_name, pet_happiness, pet_sadness)

        time.sleep(1)

if __name__ == "__main__":
    main()
