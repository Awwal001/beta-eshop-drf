from django.urls import path, reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Store

class TestProduct(APITestCase):
    url = reverse('stores')

    def test_should_create_self(self):
        user = User.objects.create_user( username="username", last_name= "last_name",  email="user@gmail.com")
        user.set_password('password123')
        user.save()

        store = Store( vendor=user, name="store name", description= "Store description")
        store.save()

        self.assertEqual(str(store), "store name")

    