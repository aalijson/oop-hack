from abstract.serializer import BaseSerializer
from models import Car

class ProductSerializer(BaseSerializer):
    class Meta:
        fields = ['id', 'brand','model','issue_year', 'engine_volume', 'color', 'body_type', 'mileage', 'price',]
        queryset = Car.objects
    
    def serialize_obj(self, obj):
        return super().serialize_obj(obj)