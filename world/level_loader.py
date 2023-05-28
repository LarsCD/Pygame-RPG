from world.level import Level

class Level_Loader:
    def __init__(self):
        pass

    def load_level(self, level_data):
        level_object = Level(level_data)
        return level_object