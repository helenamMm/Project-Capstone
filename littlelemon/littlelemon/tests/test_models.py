from django.test import TestCase
from restaurant.models import Menu

class TestMenu(TestCase):
  def test_get_item(self):
    item = Menu.objects.create(titile = 'IceCream', price = 80, inventory = 100 )
    self.assertEqual(str(item), "IceCream : 80")

