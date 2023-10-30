from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from my_app.models import People, User

PEOPLE = {"name": "Test", "last_name": "last_name", "age": 58}

USER = {"username": "Test", "password": "pass123word"}

PEOPLE_URL = reverse("my_app:index")


class TestPeopleListView(TestCase):
    def setUp(self) -> None:
        user = get_user_model().objects.create_user(**USER)
        self.client.force_login(user)

    def test_count_people(self):
        People.objects.create(name="Test", last_name="LastName", age=25)

        self.assertEqual(People.objects.count(), 1)

    def test_get_index(self):
        res = self.client.get(PEOPLE_URL)

        self.assertEqual(res.status_code, 200)


class TestUser(TestCase):
    def test_count_user(self):
        User.objects.create(
            username="test",
            first_name="Test",
            last_name="Last",
            email="email@gmail.com",
            password="Pass123word",
        )

        self.assertEqual(User.objects.count(), 1)
