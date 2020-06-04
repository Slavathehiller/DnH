from PILgraphicObject import*


class Shield(PILgraphicObject):
    ChanceToBlockModifier = 5
    PhotoImage = None

    def __init__(self, x, y):
        super().__init__(x, y)
        self.SetImage("Shield.png")

    def SetImage(self, imageFileName):
        image = Image.open(imageFileName).convert('RGBA')
        self.BaseImage = image.crop((0, 0, 25, 25))
        image2 = image.crop((25, 0, 50, 50))
        self.PhotoImage = ImageTk.PhotoImage(image2)