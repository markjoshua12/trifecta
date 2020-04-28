
from Constants import TILE_SIZE

class Engine:

    def __init__(self, entities, tiles, level, gravity: float=0.0):
        
        self.entities = entities
        self.tiles = tiles
        self.level = level

        self.gravity = gravity

    def update(self):
        
        for entity in self.entities:
            if entity.removed:
                self.entities.remove(entity)
                continue
            # if self.can_jump(entity):
            #     entity.flying = True
            # else:
            #     entity.flying = False
            if not entity.flying:
                entity.change_y -= self.gravity

            entity.update()

    def check_for_collision(self):
        pass

    def can_jump(self, entity, y_dist = 1):
        result = False

        entity.center_y -= y_dist

        tiles = self.level.get_tiles(
                int(entity.left // TILE_SIZE),
                int(entity.bottom // TILE_SIZE),
                int(entity.right // TILE_SIZE),
                int(entity.top // TILE_SIZE))

        for tile in tiles:
            if tile.is_solid and entity.intersects(tile):
                result = True
                break
        
        entity.center_y += y_dist

        return result