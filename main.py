from core import Core
from dev.dev_logger import DevLogger

class Main:
    def __init__(self):
        self.DevLogger = DevLogger()
        self.core = Core()
        self.run_game = True

    def main_loop(self):
        while self.run_game == True:
            self.core.update_game()
            self.run_game = False

if __name__ == '__main__':
    main = Main()
    main.main_loop()