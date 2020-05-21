from Consts import*
from PILgraphicObject import*
from random import*

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
    _status = Live
    DeadImage = None

    def __init__(self, x, y, model):
        PILgraphicObject.__init__(self, x, y)
        self.ResetActions()
        self.currentHealth = self.Health

    def set_Status(self, value):
        self._status = value

    def get_Status(self):
        return self._status

    Status = property(fget=get_Status, fset=set_Status)

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

    def GetCoords(self, x, y, direction, distance=1):
        newx, newy = x, y
        if direction == Up:
            newy = y - distance
        if direction == Left:
            newx = x - distance
        if direction == Down:
            newy = y + distance
        if direction == Right:
            newx = x + distance
        return newx, newy

    def Move(self, params):
        direction = params[0]
        x, y = self.GetCoords(self.x, self.y, direction)
        if direction in [Left, Right]:
            self.orientation = direction
        if self.iCanMove(x, y):
            self.Place(x, y)
            print(self.Type, "идет в точку", self.x, self.y)
        else:
            print(self.Type, "стоит в точке", self.x, self.y)

    def GetEnemyFrom(self, direction, distance=1):
        x, y = self.GetCoords(self.x, self.y, direction, distance)
        return self.model.GetActiveObjectAt(x, y)

    def Attack(self, direction, DmgModifier=0):
        enemy = self.GetEnemyFrom(direction)
        if enemy == None or enemy.Status == Dead:
            print("Нет цели")
            return
        print(self.Type + ' бьет ' + enemy.Type)
        if randint(0, 100) <= enemy.EvadeChance:
            print(enemy.Type + ' увернулся')
        else:
            damage = round(randint(self.Damage[0], self.Damage[1]) * (1 + (DmgModifier/100)))
            if randint(0, 100) < self.CriticalChance:
                damage = damage * 2
                print("Критический удар!")
            enemy.currentHealth -= damage
            print(self.Type + ' наносит ' + enemy.Type + ' ' + str(damage) + ' урона')
            if enemy.currentHealth < 1:
                enemy.Status = Dead
                print(enemy.Type + ' погибает')