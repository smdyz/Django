from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    password = models.CharField(verbose_name='пароль')

    createable = models.BooleanField(default='False', verbose_name='возможность_создания')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    telephone_number = models.CharField(verbose_name='телефон' , **NULLABLE)
    country = models.CharField(verbose_name='страна', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    # **NULLABLE заменяет null=True, blank=True (разрешает оставлять пустые ячейки)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
