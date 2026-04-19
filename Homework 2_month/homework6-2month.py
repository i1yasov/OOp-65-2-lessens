class User:

    def __init__(self,name,role):
        self.name = name
        self.role = role

def is_admin(func):
    def wrapper(user):
        if user.role == 'admin':
            return func(user)
        else:
            return 'У вас нет доступа '
    return wrapper


@is_admin
def delete_video(user):
    return f'Видео удалено'


# проверка
admin = User("Ardager", "admin")
user = User("Bek", "user")

print(delete_video(admin))
print(delete_video(user))


import time
def timer(func):
    def wrapper():
        start = time.time()
        result=func()
        end = time.time()
        duration = end - start
        print("Время выполнения:", duration)
        return result
    return wrapper

@timer
def download_video():
    print('Видео загружено')
    time.sleep(2)
download_video()
