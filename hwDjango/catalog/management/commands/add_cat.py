from typing import List, Any

from django.core.management import BaseCommand
import json
import os

from catalog.models import Category, Product


class Command(BaseCommand):

    #     Category.objects.bulk_create([
    #   {
    #     "model": "catalog.product",
    #     "pk": 11,
    #     "fields": {
    #       "name": "gorenje",
    #       "description": '',
    #       "preview": '',
    #       "category": 2,
    #       "cost": "359",
    #       "created_at": "2024-04-03",
    #       "updated_at": "2024-04-03"
    #     }
    #   },
    #   {
    #     "model": "catalog.product",
    #     "pk": 12,
    #     "fields": {
    #       "name": "hyper pc",
    #       "description": "nu takoe",
    #       "preview": '',
    #       "category": 1,
    #       "cost": "120000",
    #       "created_at": "2024-04-04",
    #       "updated_at": "2024-04-04"
    #     }
    #   }
    # ])

    @staticmethod
    def json_read_categories(path):
        # Здесь мы получаем данные из фикстурв с категориями
        with open(path, 'r', encoding='utf-16') as f:
            cat_dict = json.load(f)
        return cat_dict

    @staticmethod
    def json_read_products(path):
        # Здесь мы получаем данные из фикстурв с продуктами
        with open(path, 'r', encoding='utf-16') as f:
            prod = json.load(f)
        return prod

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        cat_path = os.path.abspath('fix_Categories.json')

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories(cat_path):
            category_for_create.append(
                Category(name=category['fields']['name'],
                         description=category['fields']['description'])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        prod_path = os.path.abspath('fix_Products.json')

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products(prod_path):
            product_for_create.append(
                Product(name=product['fields']['name'],
                        description=product['fields']['description'], preview=product['fields']['preview'],
                        category=Category.objects.get(pk=product['fields']['category']),
                        cost=product['fields']['cost'], created_at=product['fields']['created_at'],
                        updated_at=product['fields']['updated_at'])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)

# class Command(BaseCommand):
#
#     @staticmethod
#     def json_read_categories(path):
#         # Здесь мы получаем данные из фикстур с категориями
#         with open(path, 'r', encoding='utf-16') as f:
#             cat_dict = json.load(f)
#         return cat_dict
#
#     def handle(self, *args, **options):
#         Category.objects.all().delete()
#
#         cat_path = os.path.abspath('fix_Categories.json')
#         cat_list = self.json_read_categories(cat_path)
#
#         categories_for_create = []
#         for cat_item in cat_list:
#             categories_for_create.append(Category(**cat_item['fields']))
#         Category.objects.bulk_create(categories_for_create)
