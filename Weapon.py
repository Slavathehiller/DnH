import Command
from PILgraphicObject import*

class Weapon(PILgraphicObject):
    PhotoImage = None
    Name = ""
    NameTvor = ""
    StunModifier = 0
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
        PILgraphicObject.__init__(self, x, y)
        self.SetImage('sword.png')
        self.PhotoImage = ImageTk.PhotoImage(self.BaseImage)
        self.Commands = []
        self.Commands.append(Command.Stab)
        self.Commands.append(Command.Slash)

class Axe(Weapon):
    Name = "Топор"
    NameTvor = "топором"

    def __init__(self, x, y):
        PILgraphicObject.__init__(self, x, y)
        self.SetImage('axe.png')
        self.PhotoImage = ImageTk.PhotoImage(self.BaseImage)
        self.Commands = []
        self.Commands.append(Command.Slash)

class Spear(Weapon):
    Name = "Копьё"
    NameTvor = "копьём"

    def __init__(self, x, y):
        PILgraphicObject.__init__(self, x, y)
        self.SetImage('spear.png')
        self.PhotoImage = ImageTk.PhotoImage(self.BaseImage)
        self.Commands = []
        self.Commands.append(Command.LongStab)

class Mace(Weapon):
    Name = "Булава"
    NameTvor = "булавой"

    def __init__(self, x, y):
        PILgraphicObject.__init__(self, x, y)
        self.SetImage('axe.png')
        self.PhotoImage = ImageTk.PhotoImage(self.BaseImage)
        self.Commands = []
        self.Commands.append(Command.Smash)
        self.StunModifier = 25
