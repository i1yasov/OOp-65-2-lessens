#ПРОСТОЙ ДЕКОРАТОР
def simple_decorator(func):
    def wrapper():
        print('До вывода ')
        func()
        print('После вывода')
    return wrapper

@simple_decorator
def say_hello():
    print('hello world')

#say_hello()

def greeting_decorator(func):
    def wrapper(data):
        print(f'Hi  {data}')
        func(data)
    return wrapper

@greeting_decorator
def test(name):
    print(f'How are you {name} ?')
test('Beksi')
#ДЕКОРАТОРЫ С ПАРАМЕТРАМИ
def repeat_decorator(n):
    def decorator(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return decorator
@repeat_decorator(10)
def hi():
    print('Hi')
#hi()
#ДЕКОРАТОРЫ ДЛЯ КЛАССА
def class_decorator(cls):
    class NewClass(cls):
        def action(self):
            print('New action !!')
    return NewClass

@class_decorator
class OldClass:
    def action(self):
        print('Old action !!')


def is_admin(func):
    def wrapper(user):
        if user.role == 'admin':
            func()
        else:
            print('Вы не админ!!')
    return wrapper
