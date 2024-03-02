import random
from colorama import Fore, Style

class GuessingGame:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.guesses_taken = 0

    def play(self):
        print("Добро пожаловать в игру 'Угадай число'!")
        print("Я загадал число от 1 до 100.")

        while True:
            guess = input("Попробуйте угадать: ")

            try:
                guess = int(guess)
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите число.")
                continue

            self.guesses_taken += 1

            if guess < self.number:
                print(Fore.BLUE + "Слишком мало!" + Style.RESET_ALL)
            elif guess > self.number:
                print(Fore.RED + "Слишком много!" + Style.RESET_ALL)
            else:
                print(Fore.GREEN + f"Поздравляю! Вы угадали число за {self.guesses_taken} попыток." + Style.RESET_ALL)
                break

if __name__ == "__main__":
    game = GuessingGame()
    game.play()
