from Hero import*
from random import*

class Knight(Hero):

    def __init__(self, x, y, model):
        Hero.__init__(self, x, y, model)
        self.Type = 'Рыцарь'
        self.SetImage('Knight')
        self.Commands.append(self.Slash)
        self.CommandsNames.append('Рубить')
        self.Commands.append(self.Stab)
        self.CommandsNames.append('Колоть')


    def Slash(self, params):
        enemy = self.GetEnemyFrom(params[0])
        if enemy == None or enemy.Status == Dead:
            print("Нет цели")
            return
        print(self.Type + ' бьет ' + enemy.Type)
        if randint(0, 100) <= enemy.EvadeChance:
            print(enemy.Type + ' увернулся')
        else:
            damage = randint(self.Damage[0], self.Damage[1])
            if randint(0, 100) < self.CriticalChance:
                damage = damage * 2
                print("Критический удар!")
            enemy.currentHealth -= damage
            print(self.Type + ' наносит ' + enemy.Type + ' ' + str(damage) + ' урона')
            if enemy.currentHealth < 1:
                enemy.Status = Dead
                print(enemy.Type + ' погибает')

    def Stab(self, params):
        pass