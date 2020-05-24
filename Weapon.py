from Command import*
from PILgraphicObject import*

class Weapon(PILgraphicObject):
    PhotoImage = None
    Name = ""
    NameTvor = ""
    DamageModifier = 0
    ArmorPierceModifier = 0
    CritModifier = 0
    DefaultImage = None
    CanParry = False
    Commands = []

class Sword(Weapon):
    Name = "Меч"
    NameTvor = "мечом"
    CanParry = True

    def __init__(self, x, y):
        super().__init__(x, y)
        self.SetImage('sword.png')
        self.PhotoImage = ImageTk.PhotoImage(self.BaseImage)
        self.Commands.append(Slash)
        self.Commands.append(Stab)
