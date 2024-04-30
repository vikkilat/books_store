from django.db import models


class Feedback(models.Model):
    """Model of feedbacks"""
    email = models.EmailField(verbose_name='Ваш e-mail')
    name = models.CharField(max_length=100, verbose_name='Ваше имя')
    comment = models.TextField(verbose_name='Ваш комментарий')
    phone_number = models.CharField(
        max_length=12, verbose_name='Ваш номер телефона')

    def __str__(self):
        return self.name
