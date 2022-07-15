from models import Car
from views import car_create, car_delete, car_detail, car_list, car_update, comment_create
from urls import urlpatterns
from pprint import pprint
from account import User

car1 = Car('toyota', 'prius', 2005, 123.5, 'black', 'седан', 10000, 23456.45)
car2 = Car('bmw', 'x5', 2004, 150.1, 'white', 'седан', 15000, 25000.55)

# car_create()
# print(car_detail(0))
# print(car_list())

while True:
    try:
        url, arg = input("Введите адрес: ").split("/")
    except ValueError:
        print("Enter a valid url")
        continue

    found = False
    for uri, view in urlpatterns:
        if uri.split("/")[0] == url:
            found = True

            try:
                if arg:
                    pprint(view(arg))
                else:
                    pprint(view())
            except Exception as e:
                print(e)

    if not found:
        print("404 Url Not Found")