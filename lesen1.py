class Person:
    #Констуктор класса
    def __init__(self,name,hp,lvl):
        #Атрибуты класса
        self.name_Person = name
        self.hp_Person = hp
        self.lvl_Person = lvl
        #Динамические переменные
    def action(self):
        return f'{self.name_Person} base action!!'

#Обьект экземпляр на основе класса
kirito = Person('kirito',1000,100)
asuna = Person('asuna',10000,1000)
print(kirito.т )
