from Consts import *
from PILgraphicObject import *
from random import *
from Command import *
from Weapon import *


class Entity(PILgraphicObject):
    Str = 5
    Dex = 5
    End = 5
    Per = 5
    _actions = 3
    model = None
    orientation = Right
    Type = ''
    TypeRod = ''
    currentHealth = 10
    _status = Live
    DeadImage = None
    RightImage = None
    LeftImage = None
    _weapon = None
    ActionsStunCounter = 1
    SelfCommands = []
    Commands = []
    chanceToStun = 0
    WeaponPoint = (25, 0, 40, 30)
    WeaponAngle = 0

    def __init__(self, x, y, model):
        PILgraphicObject.__init__(self, x, y)
        self.ResetActions()
        self.currentHealth = self.Health
        self.model = model

    def SetImage(self, imageFileName):
        super().SetImage(imageFileName)
        self.RightImage = self.BaseImage
        self.LeftImage = self.BaseImage.transpose(Image.FLIP_LEFT_RIGHT)

    def set_ActionsCount(self, value):
        self._actions = value

    def get_ActionsCount(self):
        if self.Status == Dead or self.Status == Stun:
            self._actions = 0
        return self._actions

    ActionsCount = property(fget=get_ActionsCount, fset=set_ActionsCount)

    def set_Weapon(self, value):
        self._weapon = value
        self.Commands = list()
        self.Commands.extend(self.SelfCommands)
        if value is None:
            return
        for commandClass in value.Commands:
            self.Commands.append(commandClass(self))

    def get_Weapon(self):
        return self._weapon

    Weapon = property(fget=get_Weapon, fset=set_Weapon)

    def set_Status(self, value):
        self._status = value

    def get_Status(self):
        return self._status

    Status = property(fget=get_Status, fset=set_Status)

    def ResetActions(self):
        if self.Status == Stun:
            self.ActionsStunCounter = self.ActionsStunCounter - 1
        if self.ActionsStunCounter <= 0 or self.Status == Live:
            self.Status = Live
            self.ActionsCount = self.Actionsdef

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

    def get_ChanceToStun(self):
        cts = self.chanceToStun
        if self.Weapon is not None:
            cts = cts + self.Weapon.StunModifier
        return cts

    Health = property(fget=get_Health)
    Damage = property(fget=get_Damage)
    EvadeChance = property(fget=get_EvadeChance)
    CriticalChance = property(fget=get_CriticalChance)
    ChanceToStun = property(fget=get_ChanceToStun)
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

    def GetEnemyFrom(self, direction, distance=1):
        x, y = self.GetCoords(self.x, self.y, direction, distance)
        return self.model.GetActiveObjectAt(x, y)

    def GetCurrentImage(self):
        if self.Status == Dead:
            return self.DeadImage
        baseImage = self.BaseImage.copy()
        if self.Weapon is not None:
            weaponImg = self.Weapon.BaseImage.copy()
            weaponImg = weaponImg.rotate(self.WeaponAngle)
            baseImage.paste(weaponImg, self.WeaponPoint, weaponImg)
        if self.orientation == Right:
            return baseImage
        else:
            return baseImage.transpose(Image.FLIP_LEFT_RIGHT)
