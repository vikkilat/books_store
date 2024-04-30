from djoser.serializers import UserSerializer
from rest_framework import serializers

from books.models import Author, Book, Category, Subcategory
from feedback.models import Feedback
from users.models import User


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['email', 'name', 'comment', 'phone_number']


class UsersSerializer(UserSerializer):
    class Meta:
        model = User
        fields = (
            'email', 'id', 'username', 'first_name',
            'last_name'
        )


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title',)


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ('id', 'title',)


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
