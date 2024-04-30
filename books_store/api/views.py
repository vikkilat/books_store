from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_filters.rest_framework import DjangoFilterBackend
from djoser.views import UserViewSet
from rest_framework import viewsets

from books.models import Book, Category, Subcategory
from feedback.models import Feedback
from users.models import User

from .mixins import CreateViewSet
from .serializers import (BookSerializer, CategorySerializer,
                          FeedbackSerializer, SubcategorySerializer,
                          UsersSerializer)


class FeedbackViewSet(CreateViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    @receiver(post_save, sender=Feedback)
    def send_feedback_email(sender, instance, created, **kwargs):
        if created:
            send_mail(
                'New Feedback Received',
                f'Name: {instance.name}\nEmail:'
                f'{instance.email}\nComment:'
                f'{instance.comment}',
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_RECIPIENT],
                fail_silently=False,
            )


class UsersViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['authors',
                        'categories',
                        'title',
                        'status',
                        'publishedDate']


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['title']


class SubcategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['title']
