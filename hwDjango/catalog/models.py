from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='название_категории')
    description = models.TextField(max_length=50, verbose_name='описание_категории', **NULLABLE)

    # **NULLABLE заменяет null=True, blank=True (разрешает оставлять пустые ячейки)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        app_label = 'catalog'
        # ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.CharField(max_length=200, verbose_name='описание', **NULLABLE)
    preview = models.ImageField(verbose_name='превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория', **NULLABLE)
    cost = models.IntegerField(verbose_name='цена')
    created_at = models.CharField(verbose_name='дата создания')
    updated_at = models.CharField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        # ordering = ('name',)


class Users(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя')
    email = models.CharField(max_length=50, verbose_name='email', unique=True, **NULLABLE)
    password = models.CharField(max_length=50, verbose_name='пароль')

    createable = models.BooleanField(default='False', verbose_name='возможность_создания')

    # **NULLABLE заменяет null=True, blank=True (разрешает оставлять пустые ячейки)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        # ordering = ('name',)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_num = models.CharField(max_length=50, verbose_name='номер_версии', unique=True)
    version_name = models.CharField(max_length=50, verbose_name='имя_версии')
    sign = models.BooleanField(max_length=50, verbose_name='признак_текущей_версии')

    def __str__(self):
        return f'{self.version_name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
