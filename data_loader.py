import json
import traceback
import logging
from dev.dev_logger import DevLogger

catch_error = False

class DataLoader:
    def __init__(self):
        self.logger = DevLogger(DataLoader, print_level=logging.ERROR)

    def load_data(self, path):
        data = None
        self.logger.log(logging.INFO, f'Loading \'{path}\'')

        if catch_error:
            # load data safely
            try:
                with open(path, 'r') as file:
                    data = json.load(file)
            except Exception:
                self.logger.log(logging.ERROR, f'Failure loading \'{path}\'> {traceback.print_exc()}')
            else:
                # self.logger.log(logging.INFO, f'Successfully loaded \'{path}\'')
                pass
        else:
            # load data unsafely (not catching errors)
            with open(path, 'r') as file:
                data = json.load(file)


        return data

