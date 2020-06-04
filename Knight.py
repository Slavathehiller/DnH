from Hero import*
from Command import*

class Knight(Hero):
    Str = 6
    Dex = 8
    End = 6
    Type = 'Рыцарь'
    TypeRod = 'рыцаря'
    TypeDat = 'рыцарю'
    WeaponPoint = (17, 0, 42, 50)
    WeaponAngle = -35
    ShieldPoint = (3, 15, 28, 40)

    def __init__(self, x, y, model):
        super().__init__(x, y, model)
        self.SetImage('Knight')


