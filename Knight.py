from Hero import*
from Command import*

class Knight(Hero):
    Str = 6
    Dex = 8
    End = 6
    Type = 'Рыцарь'
    TypeRod = 'рыцаря'
    TypeDat = 'рыцарю'
    WeaponPoint = (25, 0, 40, 30)
    WeaponAngle = -35

    def __init__(self, x, y, model):
        super().__init__(x, y, model)
        self.SetImage('Knight')


