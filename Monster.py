from Entity import*
from PILgraphicObject import*

class Monster(Entity):

    def GetHeroFrom(self, direction, distance = 1):
        x, y = self.GetCoords(self.x, self.y, direction, distance)
        for hero in self.model.Heroes:
            if hero.x == x and hero.y == y:
                return hero
        return None
