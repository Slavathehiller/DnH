from Monster import*
from random import*
from Command import*

class Goathorn(Monster):
    End = 3
    Dex = 8
    Type = 'Козлорог'
    TypeRod = 'козлорога'
    TypeDat = 'козлорогу'

    def __init__(self, x, y, model):
        super().__init__(x, y, model)
        self.SetImage('Goathorn.png')
        self.DeadImage = Image.open('Goathorn_Dead.png').convert('RGBA')

    def NormalAction(self):
        for direction in [Up, Down, Left, Right]:
            hero = self.GetHeroFrom(direction)
            if not (hero is None):
                Command.Attack(self, hero)
                return
        Move(self).Run([randint(Up, Right)])





