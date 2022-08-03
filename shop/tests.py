from django.contrib.auth.models import User
from django.test import TestCase

from shop.models import Product, Payment, OrderItem, Order


# Create your tests here.
class TestDataBase(TestCase):
    fixtures = [
        "shop\\fixtures\\mydata.json"
    ]

    def setUp(self):
        self.user = User.objects.get(username='admin')

    def test_user_exists(self):
        users = User.objects.all()
        users_number = users.count()
        user = users.first()
        self.assertEqual(users_number, 2)
        self.assertEqual(user.username, 'admin')
        self.assertTrue(user.is_superuser)

    def test_user_check_password(self):
        self.assertTrue(self.user.check_password('admin'))

    def test_all_data(self):
        self.assertGreater(Product.objects.all().count(), 0)
        self.assertGreater(Order.objects.all().count(), 0)
        self.assertGreater(OrderItem.objects.all().count(), 0)
        self.assertGreater(Payment.objects.all().count(), 0)

