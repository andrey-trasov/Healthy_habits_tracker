from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from user.models import User


class UsersTestCase(APITestCase):
    """Тестирование CRUD пользователей."""

    def setUp(self):
        self.user = User.objects.create(email="foxship@yandex.ru")
        self.client.force_authenticate(user=self.user)

    def test_user_create(self):
        url = reverse("user:register")
        data = {
            "email": "foxship@zdship.ru",
            "password": "123qwe",
            "phone_number": "+7 777 777 7777",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 2)
