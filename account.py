import utils

class User:
    objects = []
    def __init__(self, email, name):
        self.email = email
        self.name = name
        self.__password = None
        self.is_authenticated = False
        print(f'Успешно создан пользователь {self.email}')
        User.objects.append(self)
    
    def register(self, password, password_confirm):
        if password != password_confirm:
            raise Exception('Пароли должны совпадать!')
        self.__password = password
        print(f'Успешно зарегестрирован пользователь {self.email}')
    
    def login(self, password):
        if self.__password != password:
            raise Exception("Пароль неверный")
        self.is_authenticated = True
        print(f'Успешно авторизовался пользователь {self.email}')

    def logout(self):
        utils.login_required(self)
        self.is_authenticated = False
        print(f"успешно вышел юзер {self.email}")

    def __str__(self):
        return self.email


        

