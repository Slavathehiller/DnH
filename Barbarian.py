from Hero import*

class Barbarian(Hero):

    def __init__(self, x, y, model):
        Hero.__init__(self, x, y, model)
        self.Type = 'Варвар'
        self.SetImage('Barbarian')
        self.Commands.append(self.Slash)
        self.CommandsNames.append('Аццки Рубить')
        self.Commands.append(self.JumpStrike)
        self.CommandsNames.append('Напрыгнуть и рубануть')


    def Slash(self, params):
        pass

    def JumpStrike(self, params):
        pass
