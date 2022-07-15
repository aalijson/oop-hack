from yaml import serialize
from models import Car, Comment
from utils import get_obj_or_404
from account import User
from serializer import ProductSerializer

def car_create():
    brand = input('Введите марку машины: ')
    model = input('Введите модель машины: ')
    issue_year = int(input('Введите год выпуска: '))
    engine_volume = round(float(input('Объем двигателя: ')), 1)
    color = input(f'Введите цвет машины {Car.colors}: ')
    body_type = input(f'Введите тип кузова{Car.body_type}: ')
    mileage = int(input('Пробег машины: '))
    price = round(float(input('Введите цену: ')), 1)

    Car(brand, model, issue_year, engine_volume, color, body_type, mileage, price)
    return print('Автомобиль успешно создан')

def car_list():
    serializer = ProductSerializer()
    cars = serializer.serialize_queryset()
    return cars
    # for i in Car.cars:
    #     print ('===', i.brand, i.model, i.issue_year, i.engine_volume, i.color, i.body_type, i.mileage, i.price,'===')

def car_detail(p_id):
    product = get_obj_or_404(Car, "id", int(p_id))
    serializer = ProductSerializer()
    return serializer.serialize_obj(product)
    # return print('~~~', product.brand, product.model, product.issue_year, product.engine_volume, product.color, product.body_type, product.mileage, product.price,'~~~')

def car_update(p_id):
    product = get_obj_or_404(Car, "id", int(p_id))
    field = input("Введите поле для изменения: ")
    if field in dir(product):
        print(f"old value: {getattr(product, field)}")
        value = input(f"{field} = ")
        setattr(product, field, value)
    else:
        raise Exception(f"Поля {field} нет в продукте")
    return car_detail(p_id)

def car_delete(p_id):
    product = get_obj_or_404(Car, "id", int(p_id))
    Car.objects.remove(product)
    return "Продукт успешно удален"

def comment_create():
    email = input("Введите email: ")
    user = get_obj_or_404(User, "email", email)
    print("Выберите брэнд продукта:")
    for p in Car.objects:
        print(p.brand)
    brand = input("=======================\n")
    product = get_obj_or_404(Car, "brand", brand)
    body = input("Введите комментарий: ")
    Comment(user, product, body)
    return print("Комментарий успешно добавлен")

def add_like(p_id):
    product = get_obj_or_404(Car, "id", int(p_id))
    product.likes += 1

