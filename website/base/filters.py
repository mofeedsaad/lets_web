import django_filters 
from .models import *

class OrderFilter(django_filters.FilterSet):
    class Meta:
        Model =Order
        fields = '__all__'