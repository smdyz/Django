from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name='заголовок')
    description = models.TextField(max_length=50, verbose_name='содержимое', **NULLABLE)
    preview = models.ImageField(verbose_name='превью', **NULLABLE)
    created_at = models.CharField(max_length=50, verbose_name='дата создания')

    published = models.BooleanField(verbose_name='опубликовано', **NULLABLE)
    views = models.IntegerField(verbose_name='просмотры', **NULLABLE)
    slug = models.CharField(max_length=100, verbose_name='slug', **NULLABLE)

    # **NULLABLE заменяет null=True, blank=True (разрешает оставлять пустые ячейки)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
