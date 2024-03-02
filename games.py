import os
import subprocess

class Games:
    def __init__(self, dir_path):
        self.dir_path = dir_path

    def startGameMode(self):
        """
        Запускает режим игры, в котором пользователь может выбирать и играть в игры.
        """
        self.run_game_mode()

    def run_game_mode(self):
        """
        Запускает режим игры, позволяя пользователю выбирать игры и возвращаться в главное меню.
        """
        while True:
            print("\nВыберите игру или введите 'exit', чтобы вернуться в главное меню:")
            self.menuGames()
            print("Введите название игры или 'exit':\n")
            game = input("--> ").lower()

            if game.lower() == 'exit':
                print("\n<ВЫХОД ИЗ РЕЖИМА ИГРЫ>")
                break
            else:
                script_path = os.path.dirname(__file__)
                self.play_game(script_path + "\\" + self.dir_path + game)

    def menuGames(self):
        """
        Выводит список доступных игр, из которых пользователь может выбрать.
        """
        files = os.listdir(self.dir_path)

        print("")

        for file in files:
            if file == "Data":
                continue
            print(">-[ " + file + " ]-<")

        print("")

    def play_game(self, game):
        """
        Пытается запустить указанную игру.

        Если игра найдена, она будет запущена. В противном случае будет выведено сообщение об ошибке.
        """

        print("\n-----------------------------------------------------------------------------\n")

        try:
            # Запуск другого скрипта
            subprocess.run(["python", game])
        except FileNotFoundError:
            print("\nОшибка: Игра не найдена.\n")
