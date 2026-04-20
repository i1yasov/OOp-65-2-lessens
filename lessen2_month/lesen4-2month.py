class Test:

    # магическим методом
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name




test_obj = Test("NAme")
test_int = 123

print(test_obj)
print(test_int)



class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.view_count = 0

    def __call__(self, *args, **kwargs):
        self.view_count += 1

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __lt__(self, other):
        print(self.x)
        print(other.x)

    def __gt__(self, other):
        print(self.x)
        print(other.x)

obj_1 = Vector(12, 13)
obj_2 = Vector(22, 23)

obj_1()


class Money:

    def __init__(self, currency, sum):
        self.currency = currency
        self.sum = sum
        self.view_count = 0

    def convert_to_coin(self, obj):
        pass

    def __add__(self, other):
        if self.currency != "coin" and other.currency != "coin":
            self.convert_to_coin(self)
            self.convert_to_coin(other)
        if self.currency != other.currency:
            pass


kg = Money("SOM", 100)
us = Money("USD", 100)


ardager_coin = kg + us

class Test:

    def __init__(self, p):
        self.p = p

    @staticmethod
    def action():
        return "action"

    def action2(self):
        return f"{self.p} action2"


test_obj = Test("P")

print(test_obj.action2())
print(Test.action())


class Money:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def concert(obj_1):
        # obj_1.sum
        return "sum"


class Bank:
    # Атрибуты класса
    bank_name = "Simba"

    def __init__(self, user_count, bank_all_money):
        # Атрибуты объекта класса
        self.user_count = user_count
        self.__bank_all_money = bank_all_money

    def get_user_count(self):
        return self.user_count

    @classmethod
    def get_bank_name(cls):
        return cls.bank_name

    @property
    def bank_money(self):
        return self.__bank_all_money

    @bank_money.setter
    def bank_money(self, value):
        if value < 0:
            raise  ValueError("Не может быть меньше 0!!")
        self.__bank_all_money = value

filial_1 = Bank(123, 1000000)
filial_2 = Bank(100, 1000000)
print(filial_1.get_user_count())
print(filial_1.bank_money)

class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0
        self.bonus = 0

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


user_1 = User("Ardager", "Kartanbekov")
user_2 = User("Ardager1", "Kartanbekov2")

print(user_1.full_name)
