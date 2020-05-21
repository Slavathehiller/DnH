from Entity import*
from Monster import*
from random import*
from time import*

class Goathorn(Monster):
    End = 3
    Dex = 8

    def __init__(self, x, y, model):
        Monster.__init__(self, x, y, model)
        self.Type = 'Козлорог'
        self.SetImage('Goathorn.png')
        self.DeadImage = Image.open('Goathorn_Dead.png').convert('RGBA')

    def NormalAction(self):
        for direction in [Up, Right]:
            hero = self.GetHeroFrom(direction)
            if not (hero is None):
                return
        self.Move([randint(Up, Right)])





