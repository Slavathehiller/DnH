from DHModeller import*
from DHViewver import*

class DHController:
    model = None
    options = None
    _currentHero = None

    def __init__(self, model, options):
        self.model = model
        self.options = options
        self.CurrentHero = self.model.Heroes[0]

    def RunCommand(self, commandIndex, params):
        self.CurrentHero.RunCommand(commandIndex, params)
        self.CurrentHero.ActionsCount = self.CurrentHero.ActionsCount - 1
        if self.CurrentHero.ActionsCount < 1:
            self.CurrentHero.ResetActions()
            self.CurrentHero = self.GetNextHero()

    def set_CurrentHero(self, value):
        self._currentHero = value
        if value is not None:
            self.model.CurrentHeroIndex = self.model.Heroes.index(value)
        else:
            self.model.CurrentHeroIndex = None

    def get_CurrentHero(self):
        return self._currentHero

    CurrentHero = property(fget=get_CurrentHero, fset=set_CurrentHero)


    def GetNextHero(self):
        i = self.model.Heroes.index(self.CurrentHero) + 1
        if i < len(self.model.Heroes):
            return(self.model.Heroes[i])
        else:
            return None

