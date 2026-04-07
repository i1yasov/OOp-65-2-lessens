# родительский класс или супер клас
class Hero:
    def __init__(self,name,level,hp):
         self.name = name
         self.level = level
         self.hp = hp

    def action(self):
        return f'{self.name} base action!!'
kirito=Hero('ardager',1,100)

    # дочерный класс
class MageHero(Hero):

    def __init__(self,name,level,hp,mp):
        super().__init__(name, level, hp)
        self.mp = mp

    def action(self):
        print(f"I'm{self.name} base action!!")

asuna = MageHero('Asuna', 1000, 10000,100000)
# Множественное наследование
class Fly:
    def action(self):
        print('Fly')

class Swim:
    def action(self):
        print('Swim')

class Animal(Fly, Swim):
    pass
dick = Animal()
# Рамбовидное Наследование
class A:
    def action(self):
        print('A')
        
class B(A):
    def action(self):
        super().action()
        print('B')
        
class C(A):
    def action(self):
        super().action()
        print('C')
        
class D (B, C):
    def action(self):
        super().action()
        print('D')
test_obj = D()
test_obj.action()
print(D.__mro__)






















