from PIL import Image, ImageTk
from Consts import*


class Command:
    ButtonImage = None
    ButtonPressedImage = None
    Name = ''

    def SetImage(self, imageFileName):
        imagefull = Image.open(imageFileName).convert('RGBA')
        image = imagefull.crop((0, 0, 50, 50))
        imagep = imagefull.crop((50, 0, 100, 50))
        self.ButtonImage = ImageTk.PhotoImage(image)
        self.ButtonPressedImage = ImageTk.PhotoImage(imagep)

    def Run(self, params):
        pass

class Move(Command):
    Name = 'Идти'

    def __init__(self):
        self.SetImage("skillimage_Move.png")

    def Run(self, params):
        entity = params[0]
        direction = params[1]
        x, y = entity.GetCoords(entity.x, entity.y, direction)
        if direction in [Left, Right]:
            entity.orientation = direction
        if entity.iCanMove(x, y):
            entity.Place(x, y)
            print(entity.Type, "идет в точку", entity.x, entity.y)
        else:
            print(entity.Type, "стоит в точке", entity.x, entity.y)

class Slash(Command):
    Name = 'Рубить'

    def __init__(self):
        self.SetImage("skillimageSlash.png")

    def Run(self, params):
        entity = params[0]
        direction = params[1]
        enemy = entity.GetEnemyFrom(direction)
        entity.Attack(entity, enemy)

class Stab(Command):
    Name = 'Колоть'

    def Run(self, params):
        entity = params[0]
        direction = params[1]
        enemy = entity.GetEnemyFrom(direction)
        entity.Attack(entity, enemy)

class JumpStrike(Command):
    Name = 'Рубануть в прыжке'

    def Run(self, params):
        entity = params[0]
        direction = params[1]
        entity.Move(params)
        enemy = entity.GetEnemyFrom(direction)
        entity.Attack(entity, enemy, DmgModifier=25)