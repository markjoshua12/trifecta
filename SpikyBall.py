
import Textures

from Enemy import Enemy

class SpikyBall(Enemy):
    def __init__(self, x, y, difficulty):
        super().__init__(Textures.get_texture(1, 1), x, y, difficulty)

        self.movespeed = 1 + difficulty * 0.2
        self.damage = 2
    
    def update(self):

        super().update()

    def move_to(self, entity):
        if self.intersects(self.level.player) and self.level.player.curr_invis_frame <= 0:
            self.die()
        if self.center_x > entity.center_x:
            self.change_x = -self.movespeed
        elif self.center_x < entity.center_x:
            self.change_x = self.movespeed
        