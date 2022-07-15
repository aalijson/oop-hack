class Car:
    objects = []
    colors = ['black', 'white', 'grey', 'red', 'brown']
    body_type = ['седан', 'универсал', 'купе', 'хэтчбек', 'минивен', 'внедорожник', 'пикап']
    id = 0
    def __init__(self, brand, model, issue_year, engine_volume, color, body_type, mileage, price, likes=0):
        self.likes = likes
        self.id = Car.id
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        self.engine_volume = engine_volume
        self.mileage = mileage
        self.price = price
        if body_type in Car.body_type:
            self.body_type = body_type
        else:
            raise Exception('There is no body type like that')
        if color in Car.colors:
            self.color = color
        else:
            raise Exception('This color is not valid')
        Car.objects.append(self)
        Car.id += 1

class Comment:
    objects = []

    def __init__(self, user, product, body):
        from datetime import datetime
        self.user = user
        self.product = product
        self.body = body
        self.created_at = datetime.now()
        Comment.objects.append(self)
