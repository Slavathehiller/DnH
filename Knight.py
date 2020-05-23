from Hero import*
from Command import*

class Knight(Hero):
    Str = 6
    Dex = 8
    End = 6

    def __init__(self, x, y, model):
        Hero.__init__(self, x, y, model)
        self.Type = 'Рыцарь'
        self.SetImage('Knight')
        self.Commands.append(Slash())
        #self.Commands.append(Stab())

