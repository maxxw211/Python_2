from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.exceptions import ErrorDetail

from sales_manager.models import Book
import json

class SalesTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("test_name")

    def test_create_book(self):
        url = reverse("create-book")
        self.client.force_login(self.user)
        data = {
            "title": "test title",
            "text": "test text",
            "author": self.user.id
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], data["title"])
        self.assertEqual(response.data["text"], data["text"])
        self.assertEqual(response.data["author"], data["author"])
        book = Book.objects.get(**data)
        self.assertEqual(response.data["id"], book.id)

    def test_update(self):
        book = Book.objects.create(title="test", author=self.user)


class SetRateBookTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user("test_name")
        self.user2 = User.objects.create_user("test_name2")
        self.book = Book.objects.create(
            title="test",
            text="test text",
            author=self.user
        )

    def test_rate(self):
        self.client.force_login(self.user)
        url = reverse("add-rate-book")
        data = {
            "rate": 3,
            "book_id": self.book.id
        }
        # good case
        response = self.client.put(url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.data)
        self.assertEqual(response.data["avg_rate"], 3)
        # check other user good case
        self.client.force_login(self.user2)
        data["rate"] = 5
        response = self.client.put(url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.data)
        self.assertEqual(response.data["avg_rate"], 4)
        # check 400 msg
        data.pop("rate")
        response = self.client.put(url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg=response.data)
        self.assertEqual(response.data["rate"][0], ErrorDetail(string='Обязательное поле.', code='required'))
        # check 400 again
        data["rate"] = 45
        response = self.client.put(url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.client.logout()
        # check 403 msg
        data["rate"] = 5
        response = self.client.put(url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)