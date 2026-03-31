class Hero :
    # Констуктор класса
    def __init__(self,name,level,health,strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength
    # Динамические переменные
    def greet (self) :
        return f'Привет, я {self.name}, мой уровень {self.level}'
    def attack (self) :
        self.strength -= 1
        return  f'{self.name} наносит удар , мое сила   {self.strength}'
    def rest (self) :
        self.health += 1
        return  f'{self.name} отдыхает , мое здаровье {self.health}   '
    #Обьект экземпляр на основе класса
naruto = Hero('naruto',99,100,100)
kakashi = Hero('kakashi',70,100,100)
obito = Hero('obito',80,100,100)
saske = Hero('saske',90,100,100)
itachi = Hero('itachi',70,100,100)

    # Вызвать у каждого объекта все созданные методы.
print(naruto.greet()) #Привет, я naruto, мой уровень 99
print(itachi.attack()) #itachi наносит удар , мое сила   99
print(saske.rest())  #saske отдыхает , мое здаровье 101
