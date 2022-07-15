def get_obj_or_404(car, attr, val):
    found = False

    for obj in car.objects:
        obj_val = getattr(obj, attr)
        if obj_val == val:
            found = True
            break

    if not found:
        raise Exception(f'404 {car.__name__} Not Found')

    return obj

def login_required(obj):
    if not obj.is_authenticated:
        raise Exception('Пользователь не авторизован')