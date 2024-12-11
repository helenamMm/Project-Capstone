from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking
from .serializers import MenuSerializers, BookingSerializers
# Create your views here.
def index(request):
  return render(request, 'index.html', {})

class MenuItemView(ListCreateAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializers

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializers

class BookingViewSet(ModelViewSet):
  queryset = Booking.objects.all()
  serializer_class = BookingSerializers
  permission_classes = [IsAuthenticated]


