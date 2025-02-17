from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        item2 =  Menu.objects.create(title="IceCream 2", price=70, inventory=10)

    def test_getall(self):
        item = Menu.objects.all()
        print(item.count())

        item1 = item[:1].get()
        print(item1)
        self.assertEqual(item1, 'IceCream : 80.00')