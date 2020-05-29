from Hero import*
from Command import*

class Barbarian(Hero):
    Str = 8
    Dex = 6
    End = 8
    Type = 'Варвар'
    TypeRod = 'варвара'
    TypeDat = 'варвару'
    WeaponPoint = (25, 0, 50, 50)
    WeaponAngle = 20

    def __init__(self, x, y, model):
        super().__init__(x, y, model)
        self.SetImage('Barbarian')
        self.SelfCommands.append(JumpStrike(self))
        self.Commands.append(JumpStrike(self))


