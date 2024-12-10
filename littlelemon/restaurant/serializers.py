from rest_framework import serializers
from .models import Menu, Booking
class MenuSerializers(serializers.ModelSerializer):
  class Meta:
        model = Menu
        fields = ['id', 'titile', 'price', 'inventory']
        extra_kwargs = {
             'price': {'min_value': 2}, 
             'inventory':{'min_value': 0}
        }

class BookingSerializers(serializers.ModelSerializer):
     class Meta:
         model = Booking
         fields = '__all__'