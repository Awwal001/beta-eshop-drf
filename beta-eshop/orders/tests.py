from django.urls import path, reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Order

class TestProduct(APITestCase):
    url = reverse('orders')

    def test_should_create_self(self):
        user = User.objects.create_user( username="username", last_name= "last_name",  email="user@gmail.com")
        user.set_password('password123')
        user.save()

        order = Order( user=user, shippingAddress="shippingAddress", totalPrice= "199.99", items= [])
        order.save()

        self.assertEqual(str(order), "shippingAddress")