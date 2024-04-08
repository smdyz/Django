from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='название_категории')
    description = models.TextField(max_length=50, verbose_name='описание_категории', **NULLABLE)

    # **NULLABLE заменяет null=True, blank=True (разрешает оставлять пустые ячейки)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
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
        return f'{self.name} {self.description} {self.category} {self.cost}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        # ordering = ('name',)