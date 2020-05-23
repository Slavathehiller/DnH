from Hero import*
from Command import*

class Barbarian(Hero):
    Str = 8
    Dex = 6
    End = 8

    def __init__(self, x, y, model):
        Hero.__init__(self, x, y, model)
        self.Type = 'Варвар'
        self.SetImage('Barbarian')
        self.Commands.append(Slash())
        #self.Commands.append(JumpStrike())


