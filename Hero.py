from PILgraphicObject import*
from Entity import*
from Consts import*
from Command import*

class Hero(Entity):
    PresenterImage = None
    Commands = []
    CommandsNames = []

    def __init__(self, x, y, model):
        Entity.__init__(self, x, y, model)
        self.model = model
        self.Commands = [Move()]
        self.CommandsNames = ["Идти"]

    def SetImage(self, imageFileName):
        PILgraphicObject.SetImage(self, imageFileName + '.png')
        image = Image.open(imageFileName + '_Presenter.png')
        self.PresenterImage = ImageTk.PhotoImage(image)


    def RunCommand(self, commandIndex, params):
        command = self.Commands[commandIndex]
        command.Run(params)
