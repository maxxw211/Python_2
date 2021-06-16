from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField

from sales_manager.models import Book


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class BookSerializer(ModelSerializer):
  #  author = AuthorSerializer()
  #  username = CharField(source="author.username")

    class Meta:
        model = Book
        fields = ["title", "text", "img", "author", "id"]



