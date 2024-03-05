# Generated by Django 4.2 on 2024-03-05 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Ваш e-mail')),
                ('name', models.CharField(max_length=100, verbose_name='Ваше имя')),
                ('comment', models.TextField(verbose_name='Ваш комментарий')),
                ('phone_number', models.CharField(max_length=12, verbose_name='Ваш номер телефона')),
            ],
        ),
    ]
