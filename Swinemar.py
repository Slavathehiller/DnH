from DHController import*
from Monster import*
from Command import*

class Swinemar(Monster):
    End = 8
    Dex = 4
    Type = 'Свиноморф'
    TypeRod = 'свиноморфа'
    TypeDat = 'свиноморфу'

    def __init__(self, x, y, model):
        super().__init__(x, y, model)
        self.SetImage('Swinemar.png')
        self.DeadImage = Image.open('Goathorn_Dead.png').convert('RGBA')
        self.SelfCommands.append(FangStrike(self))
        self.Commands.append(FangStrike(self))

    def NormalAction(self):
        for direction in [Up, Down, Left, Right]:
            hero = self.GetHeroFrom(direction)
            if not (hero is None):
                self.RunCommand(0, [direction])
                return
        Move(self).Run([randint(Up, Right)])
