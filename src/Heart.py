
import Textures

from Mob import Mob

class Heart(Mob):
    def __init__(self, x, y):
        super().__init__(Textures.get_texture(4, 9), x, y)

    def update(self):

        if self.intersects(self.level.player):
            if self.level.player.health < self.level.player.max_health:
                self.level.player.heal(3)
                self.removed = True

        super().update()

    def create_hit_box(self):
        import Maths
        self.set_hit_box(Maths.create_hit_box(10, 10))