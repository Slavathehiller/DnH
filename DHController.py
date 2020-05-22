from DHModeller import*
from DHViewver import*

class DHController:
    model = None
    options = None
    currentHero = None

    def __init__(self, model, options):
        self.model = model
        self.options = options
        self.currentHero = self.model.Heroes[0]

    def RunCommand(self, commandIndex, params):
        self.currentHero.RunCommand(commandIndex, params)
        self.currentHero.actions = self.currentHero.actions - 1
        if self.currentHero.actions < 1:
            self.currentHero.ResetActions()
            self.currentHero = self.GetNextHero()

    def GetNextHero(self):
        i = self.model.Heroes.index(self.currentHero) + 1
        if i < len(self.model.Heroes):
            return(self.model.Heroes[i])
        else:
            return None
