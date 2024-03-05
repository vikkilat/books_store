from django.core.validators import MinValueValidator
from django.db import models


class Author(models.Model):
    """Model of autors"""
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    """Model of categories"""
    slug = models.SlugField(
        null=False,
        blank=False,
        unique=True
    )
    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True
    )

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return self.title


class Subcategory(models.Model):
    """Model of subcategories"""
    slug = models.SlugField(
        null=False,
        blank=False,
        unique=True
    )
    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.title


class Book(models.Model):
    """Model of books"""
    title = models.TextField(max_length=100,)
    isbn = models.CharField(max_length=13, unique=True,)
    pageCount = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), ],)
    publishedDate = models.DateTimeField(auto_now_add=True,)
    thumbnailUrl = models.ImageField(
        upload_to='books/',
    )
    shortDescription = models.CharField(max_length=1000,)
    longDescription = models.TextField()
    status = models.CharField(max_length=255,)
    authors = models.ManyToManyField(
        Author, related_name='author_of_book',
    )
    categories = models.ManyToManyField(
        Category, related_name='category_of_book',
    )
