from PIL import Image, ImageTk
from Consts import*
from Weapon import*
from random import*


class Command:
    ButtonImage = None
    ButtonPressedImage = None
    Name = ''
    entity = None
    NameTvor = ''

    def __init__(self, entity):
        self.entity = entity

    def SetImage(self, imageFileName):
        imagefull = Image.open(imageFileName).convert('RGBA')
        image = imagefull.crop((0, 0, 50, 50))
        imagep = imagefull.crop((50, 0, 100, 50))
        self.ButtonImage = ImageTk.PhotoImage(image)
        self.ButtonPressedImage = ImageTk.PhotoImage(imagep)

    def Run(self, params):
        pass

    @staticmethod
    def Attack(attacker, target, DmgModifier=0, StunModifier=0, CommandTvor=''):
        if target == None or target.Status == Dead:
            print("Нет цели")
            return
        Message = attacker.Type + ' бьет ' + target.TypeRod
        if attacker.Weapon is not None:
            Message = Message + " " + attacker.Weapon.NameTvor
        else:
            Message = Message + " " + CommandTvor
        print(Message)
        if randint(0, 100) <= target.EvadeChance:
            print(target.Type + ' увернулся')
        else:
            damage = round(randint(attacker.Damage[0], attacker.Damage[1]) * (1 + (DmgModifier/100)))
            if randint(0, 100) < attacker.CriticalChance:
                damage = damage * 2
                print("Критический удар!")
            armorModifier = 0
            if target.Helm is not None:
                armorModifier = armorModifier + target.Helm.ArmorModifier
            if target.Torso is not None:
                armorModifier = armorModifier + target.Torso.ArmorModifier
            if target.HeavyTorso is not None:
                armorModifier = armorModifier + target.HeavyTorso.ArmorModifier
            damage = round(damage * (1 - armorModifier/100))
            if randint(0, 100) < attacker.ChanceToStun + StunModifier:
                if target.Helm is None or randint(0, 100) > target.Helm.StunChanceReduce:
                    target.Status = Stun
                    print(target.Type + " оглушен!")
            target.currentHealth -= damage
            print(attacker.Type + ' наносит ' + target.TypeDat + ' ' + str(damage) + ' урона')
            if target.currentHealth < 1:
                target.Status = Dead
                print(target.Type + ' погибает')

class Move(Command):
    Name = 'Идти'

    def __init__(self, entity):
        super().__init__(entity)
        self.SetImage("skillimage_Move.png")

    def Run(self, params):
        direction = params[0]
        x, y = self.entity.GetCoords(self.entity.x, self.entity.y, direction)
        if direction in [Left, Right]:
            self.entity.orientation = direction
        if self.entity.iCanMove(x, y):
            self.entity.Place(x, y)
            print(self.entity.Type, "идет в точку", self.entity.x, self.entity.y)
        else:
            print(self.entity.Type, "стоит в точке", self.entity.x, self.entity.y)


class Slash(Command):
    Name = 'Рубить'

    def __init__(self, hero):
        super().__init__(hero)
        self.SetImage("skillimageSlash.png")

    def Run(self, params):
        direction = params[0]
        enemy = self.entity.GetEnemyFrom(direction)
        Command.Attack(self.entity, enemy)

class Smash(Command):
    Name = 'Бить'

    def __init__(self, hero):
        super().__init__(hero)
        self.SetImage("skillimageSlash.png")

    def Run(self, params):
        direction = params[0]
        enemy = self.entity.GetEnemyFrom(direction)
        Command.Attack(self.entity, enemy)

class Stab(Command):
    Name = 'Колоть'

    def __init__(self, hero):
        super().__init__(hero)
        self.SetImage("skillimageStab.png")

    def Run(self, params):
        direction = params[0]
        enemy = self.entity.GetEnemyFrom(direction)
        Command.Attack(self.entity, enemy)

class LongStab(Command):
    Name = 'Выпад и укол'

    def __init__(self, hero):
        super().__init__(hero)
        self.SetImage("skillimageStab.png")

    def Run(self, params):
        direction = params[0]
        enemy = self.entity.GetEnemyFrom(direction)
        if enemy is None:
            enemy = self.entity.GetEnemyFrom(direction, distance=2)
        Command.Attack(self.entity, enemy)

class JumpStrike(Command):
    Name = 'Рубануть в прыжке'

    def __init__(self, hero):
        super().__init__(hero)
        self.SetImage("skillimageJumpStrike.png")

    def Run(self, params):
        direction = params[0]
        Move(self.entity).Run(params)
        enemy = self.entity.GetEnemyFrom(direction)
        Command.Attack(self.entity, enemy, DmgModifier=25)

class SmashHorn(Command):
    Name = 'Удар рогами'
    NameTvor = 'рогами'

    def Run(self, params):
        direction = params[0]
        enemy = self.entity.GetHeroFrom(direction)
        Command.Attack(self.entity, enemy, StunModifier=25, CommandTvor=self.NameTvor)

class SmashClaws(Command):
    Name = 'Удар когтями'
    NameTvor = 'когтями'

    def Run(self, params):
        direction = params[0]
        enemy = self.entity.GetHeroFrom(direction)
        Command.Attack(self.entity, enemy, CommandTvor=self.NameTvor)
