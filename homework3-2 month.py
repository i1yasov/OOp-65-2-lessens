from abc import ABC, abstractmethod
class Hero(ABC):
    def __init__(self,name,lvl,health,strength):
        self.name=name
        self.lvl=lvl
        self.__health=health # privat otrebut
        self.strength=strength

    def greet(self):
        return f'Привет, я {self.name}, мой уровень {self.lvl}'

    def rest(self):
        self.__health += 1
        return f'{self.name} отдыхает'

    @abstractmethod
    def attack(self):
        pass

class Warrior(Hero):
    def attack(self):
        return f'Воин атакует мечом'

class Mage(Hero):
    def attack(self):
        return f'Маг использует магию'

class Assassin(Hero):
    def attack(self):
        return f'Ассасин атакует из-под тишка'
warrior = Warrior("Torson",60,100,20)
mage = Mage('Rudeus',55,100,30)
assassin = Assassin('Shedow',75,100,50)


for hero in [warrior, mage, assassin]:
    print(hero.greet())
    print(hero.attack())
    print(hero.rest())
    print("------")