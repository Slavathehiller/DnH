from Monster import*
class DHModeller:
    Monsters = []
    Heroes = []
    Options = None

    def __init__(self, heroes, monsters, options):
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
        activeObject = list()
        #activeObject.extend(self.Heroes)
        activeObject.extend(self.Monsters)
        return activeObject

    ActiveObjects = property(fget=GetActiveObjects)

    def GetAllObjects(self):
        allObjects = list()
        allObjects.extend(self.Heroes)
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
        for activeobject in self.ActiveObjects:
            activeobject.NormalAction()