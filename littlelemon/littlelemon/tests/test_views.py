from django.test import TestCase
from restaurant.models import Menu
from rest_framework.test import APIClient
from restaurant.serializers import MenuSerializers
class TestMenuView(TestCase):
  def setUp(self):
    self.item1 = Menu.objects.create(titile = 'IceCream', price = 80, inventory = 100)
    self.item2 = Menu.objects.create(titile = 'Panetone', price = 50, inventory = 100)
    self.client = APIClient()

  def test_get_all_items(self):
        response = self.client.get('/restaurant/menu/')
        items = Menu.objects.all()
        serialized_items = MenuSerializers(items, many=True).data
        self.assertEqual(len(items), 2)  
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), serialized_items)
