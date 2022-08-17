from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class TestProduct(APITestCase):
    url = "api/users/"

    def test_should_create_self(self):
        user = User.objects.create_user( username="username", last_name= "last_name",  email="user@gmail.com")
        user.set_password('password123')
        user.save()

        self.assertEqual(str(user), "username")