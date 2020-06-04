from PILgraphicObject import*
from Entity import*
from Consts import*
from Command import*


class Hero(Entity):
    PresenterImage = None

    def __init__(self, x, y, model):
        super().__init__(x, y, model)
        self.model = model
        self.Commands = []
        self.SelfCommands = [Move(self)]
        self.Commands.extend(self.SelfCommands)

    def SetImage(self, imageFileName):
        super().SetImage(imageFileName + '.png')
        image = Image.open(imageFileName + '_Presenter.png')
        self.PresenterImage = ImageTk.PhotoImage(image)

