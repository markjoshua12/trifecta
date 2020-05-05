
from src import Textures

from src.entity.Mob import Mob

class Obelisk(Mob):
    def __init__(self, x, y):
        super().__init__(Textures.get_texture(0, 0), x, y)\


    def grabbed(self, entity):
        self.level.difficulty += 1
        self.level.reset()
        self.level.generate_level(self.center_x, self.center_y)