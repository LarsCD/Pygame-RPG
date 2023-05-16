from core import Core

class Main:
    def __init__(self):
        self.core = Core()
        self.run_game = True

    def main_loop(self):
        while self.run_game == True:
            self.core.update_game()
            self.run_game = False

if __name__ == '__main__':
    main = Main()
    main.main_loop()