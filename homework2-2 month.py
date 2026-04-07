class Hero :
    def __init__(self, name , lvl,hp,strength):
        self.name = name # имя
        self.lvl = lvl # уровень
        self.hp = hp # здаровье
        self.strength =strength # сила
    def greet(self):
        return f'Привет я герой {self.name}  '
    def attack(self):
        pass
    def rest (self):
        return f"Герой {self.name} отдыхает и востанавливает здоровье   "

class Warrior(Hero) :
    def __init__(self, name ,lvl,hp,strength,stamina):
        super().__init__(name,lvl,hp,strength)
        self.stamina = stamina
    def attack(self):
        return f'Воин {self.name} атакует мечом!'

class Mage(Hero) :
    def __init__(self, name , lvl,hp,strength,mana):
        super().__init__(name,lvl,hp,strength)
        self.mana = mana
    def attack(self):
        return f'Маг {self.name} кастует заклинание!'


class Assassin(Hero) :
    def __init__(self, name , lvl,hp,strength,stealth):
        super().__init__(name,lvl,hp,strength)
        self.stealth = stealth
    def attack(self):
        return f'Ассасин {self.name} атакует из-под тишка !!'
warrior = Warrior('Torsan',50,50,50,50)
mage = Mage('Rudeus',50,50,50,50)
assassin = Assassin('Shedow',50,50,50,50)
print(warrior.greet())
print(mage.attack())
print(assassin.rest())

import random

# Родительский класс
class Hero:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


# Наследники
class Warrior(Hero):
    pass


class Assassin(Hero):
    pass


class Mage(Hero):
    pass


# Создаем героев
heroes = {
    "warrior": Warrior("Warrior"),
    "assassin": Assassin("Assassin"),
    "mage": Mage("Mage")
}

# Правила победы
wins = {
    "warrior": "assassin",
    "assassin": "mage",
    "mage": "warrior"
}

# 1. Выбор игрока
choice = input("Выберите героя (Warrior / Mage / Assassin): ").lower()

if choice not in heroes:
    print("Ошибка выбора!")
else:
    player = heroes[choice]

    # 2. Случайный противник
    enemy_key = random.choice(list(heroes.keys()))
    enemy = heroes[enemy_key]

    print(f"\nВы выбрали: {player}")
    print(f"Противник: {enemy}")

    # 3. Определяем победителя
    if choice == enemy_key:
        print("Ничья!")
    elif wins[choice] == enemy_key:
        print(f"{player} победил!")
    else:
        print(f"{enemy} победил!")