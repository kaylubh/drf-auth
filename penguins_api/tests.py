from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Penguin


class PenguinTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_penguin = Penguin.objects.create(
            name="penguin",
            user=testuser1,
            species="gentoo",
            description="penguin description",
        )
        test_penguin.save()

    def setUp(self):
        self.client.login(username="testuser1", password="pass")

    def test_penguins_model(self):
        penguin = Penguin.objects.get(id=1)
        actual_user = str(penguin.user)
        actual_name = str(penguin.name)
        actual_species = str(penguin.species)
        actual_description = str(penguin.description)
        self.assertEqual(actual_user, "testuser1")
        self.assertEqual(actual_name, "penguin")
        self.assertEqual(actual_species, "gentoo")
        self.assertEqual(
            actual_description, "penguin description"
        )

    def test_get_penguin_list(self):
        url = reverse("penguin_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        penguins = response.data
        self.assertEqual(len(penguins), 1)
        self.assertEqual(penguins[0]["name"], "penguin")

    def test_get_penguin_by_id(self):
        url = reverse("penguin_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        penguin = response.data
        self.assertEqual(penguin["name"], "penguin")

    def test_create_penguin(self):
        url = reverse("penguin_list")
        data = {"user": 1, "name": "penguin2", "species": "chinstrap", "description": "penguin description2"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        penguins = Penguin.objects.all()
        self.assertEqual(len(penguins), 2)
        self.assertEqual(Penguin.objects.get(id=2).name, "penguin2")

    def test_update_penguin(self):
        url = reverse("penguin_detail", args=(1,))
        data = {
            "user": 1,
            "name": "penguin",
            "species": "gentoo",
            "description": "not a penguin",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        penguin = Penguin.objects.get(id=1)
        self.assertEqual(penguin.name, data["name"])
        self.assertEqual(penguin.user.id, data["user"])
        self.assertEqual(penguin.description, data["description"])

    def test_delete_penguin(self):
        url = reverse("penguin_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        penguins = Penguin.objects.all()
        self.assertEqual(len(penguins), 0)
