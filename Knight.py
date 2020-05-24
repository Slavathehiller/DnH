from Hero import*
from Command import*

class Knight(Hero):
    Str = 6
    Dex = 8
    End = 6
    Type = 'Рыцарь'
    TypeRod = 'рыцаря'
    TypeDat = 'рыцарю'

    def __init__(self, x, y, model):
        super().__init__(x, y, model)
        self.SetImage('Knight')


