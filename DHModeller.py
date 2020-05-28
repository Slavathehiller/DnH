from Entity import*
from Monster import*


class DHModeller:
    Monsters = []
    Heroes = []
    Options = None
    CurrentHeroIndex = None

    def __init__(self, heroes, monsters, options):
        for hero in heroes:
            hero.model = self
        for monster in monsters:
            monster.model = self
        self.Heroes = heroes
        self.Monsters = monsters
        self.Options = options

    def GetObjectsAt(self, x, y):
        objects = list()
        for currentObject in self.AllObjects:
            if currentObject.x == x and currentObject.y == y:
                objects.append(currentObject)
        return objects

    def GetActiveObjectAt(self, x, y):
        for currentObject in self.ActiveObjects:
            if currentObject.x == x and currentObject.y == y:
                return currentObject

    def GetActiveObjects(self):
        activeObjects = list()
        for monster in self.Monsters:
            if monster.Status != Dead:
                activeObjects.append(monster)
        return activeObjects

    ActiveObjects = property(fget=GetActiveObjects)

    def GetStaticObjects(self):
        staticObjects = list()
        for monster in self.Monsters:
            if monster.Status == Dead:
                staticObjects.append(monster)
        return staticObjects

    StaticObjects = property(fget=GetStaticObjects)

    def GetAllObjects(self):
        allObjects = list()
        allObjects.extend(self.Heroes)
        allObjects.extend(self.StaticObjects)
        allObjects.extend(self.ActiveObjects)
        return allObjects

    AllObjects = property(fget=GetAllObjects)

    def isMonster(self, x, y):
        activeObject = self.GetActiveObjectAt(x, y)
        return (activeObject is not None) and isinstance(activeObject, Monster)

    def isHero(self, x, y):
        for hero in self.Heroes:
            if hero.x == x and hero.y == y:
                return True
        return False

    def isOut(self, x, y):
        return x < 0 or y < 0 or x > self.Options.sizeX - 1 or y > self.Options.sizeY - 1

    def tic(self):
        for i in range(len(self.ActiveObjects)):
            activeobject = self.ActiveObjects[i]
            if activeobject.actions > 0:
                activeobject.NormalAction()
                activeobject.actions = activeobject.actions - 1
                return CYCLING
        for activeobject in self.ActiveObjects:
            activeobject.ResetActions()
        return ENDOFCYCLE