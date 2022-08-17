from django.urls import path, reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Store, Product

class TestProduct(APITestCase):
    url = reverse('products')

    def test_should_create_self(self):
        user = User.objects.create_user( username="username", last_name= "last_name",  email="user@gmail.com")
        user.set_password('password123')
        user.save()

        store = Store( vendor=user, name="store name", description= "Store description")
        store.save()

        product = Product(store= store, name="Airforce1", image= "image.png", price=99.99, brand="nike", countInStock=5, category="shoes", description="description")
        product.save()

        self.assertEqual(str(product), "Airforce1")

    
    def test_get_products(self):

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)