from PILgraphicObject import*
from Consts import*

class Armor(PILgraphicObject):
    ArmorModifier = 0
    BodyPart = -1
    PhotoImage = None
    StunChanceReduce = 0

    def SetImage(self, imageFileName):
        image = Image.open(imageFileName).convert('RGBA')
        self.BaseImage = image
        self.PhotoImage = ImageTk.PhotoImage(image)


class LightHelm(Armor):
    ArmorModifier = 10
    StunChanceReduce = 10
    BodyPart = BPHEAD

    def __init__(self, x, y):
        super().__init__(x, y)
        self.SetImage("LightHelm.png")

class HeavyHelm(Armor):
    ArmorModifier = 20
    StunChanceReduce = 30
    BodyPart = BPHEAD

    def __init__(self, x, y):
        super().__init__(x, y)
        self.SetImage("HeavyHelmet.png")


class LightArmor(Armor):
    ArmorModifier = 25
    BodyPart = BPCHEST

    def __init__(self, x, y):
        super().__init__(x, y)
        self.SetImage("LightArmor.png")

class HeavyArmor(Armor):
    ArmorModifier = 50
    BodyPart = BPCHEST

    def __init__(self, x, y):
        super().__init__(x, y)
        self.SetImage("HeavyArmor.png")


