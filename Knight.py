from Hero import*
from random import*

class Knight(Hero):
    Str = 6
    Dex=8
    End = 6

    def __init__(self, x, y, model):
        Hero.__init__(self, x, y, model)
        self.Type = 'Рыцарь'
        self.SetImage('Knight')
        self.Commands.append(self.Slash)
        self.CommandsNames.append('Рубить')
        self.Commands.append(self.Stab)
        self.CommandsNames.append('Колоть')


    def Slash(self, params):
        self.Attack(params)

    def Stab(self, params):
        pass