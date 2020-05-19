from Consts import*
from PILgraphicObject import*

class Entity(PILgraphicObject):
    Str = 5
    Dex = 5
    End = 5
    Per = 5
    actions = 3
    model = None
    orientation = Right
    Type = ''
    currentHealth = 10
    Status = Live
    DeadImage = None

    def __init__(self, x, y, model):
        PILgraphicObject.__init__(self, x, y)
        self.ResetActions()
        self.currentHealth = self.Health

    def GetCurrentImage(self):
        if self.Status == Live:
            return self.BaseImage
        if self.Status == Dead:
            return self.DeadImage

    def ResetActions(self):
        self.actions = self.Actionsdef

    def get_Health(self):
        return self.End * 10

    def get_Damage(self):
        return [self.Str // 2, self.Str]

    def get_EvadeChance(self):
        return self.Dex * 2

    def get_CriticalChance(self):
        return self.Per * 2

    def get_Actionsdef(self):
        return self.Dex // 2

    Health = property(fget=get_Health)
    Damage = property(fget=get_Damage)
    EvadeChance = property(fget=get_EvadeChance)
    CriticalChance = property(fget=get_CriticalChance)
    Actionsdef = property(fget=get_Actionsdef)

    def Place(self, x, y):
        self.x = x
        self.y = y

    def iCanMove(self, x, y):
        return not self.model.isOut(x, y) and not self.model.isHero(x, y) and not self.model.isMonster(x, y)

    def GetCoords(self, x, y, direction, distance = 1):
        newx, newy = x, y
        if direction == Up:
            newy = self.y - distance
        if direction == Left:
            newx = self.x - distance
            self.orientation = direction
        if direction == Down:
            newy = self.y + distance
        if direction == Right:
            newx = self.x + distance
            self.orientation = direction
        return newx, newy

    def Move(self, params):
        direction = params[0]
        x, y = self.GetCoords(self.x, self.y, direction)
        if self.iCanMove(x, y):
            self.Place(x, y)

    def GetEnemyFrom(self, direction, distance=1):
        x, y = self.GetCoords(self.x, self.y, direction, distance)
        return self.model.GetActiveObjectAt(x, y)
