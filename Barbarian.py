from Hero import*

class Barbarian(Hero):
    Str = 8
    Dex = 6
    End = 8

    def __init__(self, x, y, model):
        Hero.__init__(self, x, y, model)
        self.Type = 'Варвар'
        self.SetImage('Barbarian')
        self.Commands.append(self.Slash)
        self.CommandsNames.append('Аццки Рубить')
        self.Commands.append(self.JumpStrike)
        self.CommandsNames.append('Напрыгнуть и рубануть')


    def Slash(self, params):
        self.Attack(params[0])

    def JumpStrike(self, params):
        self.Move(params)
        self.Attack(params[0], 25)
