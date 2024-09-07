from django.urls import reverse

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from tracker.models import Habit
from user.models import User


class HabitTestCase(APITestCase):
    """Тестирование CRUD привычек."""

    def setUp(self):
        self.user = User.objects.create(email="foxship@yandex.ru")
        self.habit = Habit.objects.create(
            name="шоколадка",
            place="Дома",
            action="ем 2 шоколадки",
            first_time_to_do="2024-08-18T13:01:13.605876Z",
            is_pleasant="True",
            periodicity=1,
            duration="00:02:00",
            is_public="True",
            is_active="True",
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_list(self):
        url = reverse("tracker:habit")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_create(self):
        url = reverse("tracker:habit_create")
        data = {
            "name": "Отжимания",
            "place": "Дома",
            "action": "Утром отжимаюсь от пола 50 раз",
            "first_time_to_do": "2024-08-18T13:01:13.605876Z",
            "is_pleasant": "False",
            "periodicity": 1,
            "duration": "00:02:00",
            "is_public": "True",
            "is_active": "True",
            "owner": self.user.pk,
            "relation_habit": 1,
        }

        # data = {
        #     "name": "шоколадка",
        #     "place": "Дома",
        #     "action": "ем 2 шоколадки",
        #     "first_time_to_do": "2024-08-18T13:01:13.605876Z",
        #     "is_pleasant": "True",
        #     "periodicity": 1,
        #     "duration": "00:02:00",
        #     "is_public": "True",
        #     "is_active": "True",
        #     "owner": self.user.pk,
        # }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_retrieve(self):
        url = reverse("tracker:habit_detail", args=(self.habit.pk,))
        response = self.client.get(url)
        # data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(data.get("period"), self.habit.period)

    def test_habit_update(self):
        url = reverse("tracker:habit_update", args=(self.habit.pk,))
        data = {
            "name": "шоколадка",
            "place": "Дома",
            "action": "ем 1 шоколадку",
            "first_time_to_do": "2024-08-18T13:01:13.605876Z",
            "is_pleasant": "True",
            "periodicity": 1,
            "duration": "00:02:00",
            "is_public": "True",
            "is_active": "True",
            "owner": self.user.pk,
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), "Дома")

    def test_habit_delete(self):
        url = reverse("tracker:habit_delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_public_list(self):
        url = reverse("tracker:habit_public")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
