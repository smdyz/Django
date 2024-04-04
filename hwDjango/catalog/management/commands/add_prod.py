from django.core.management import BaseCommand
import json
import os

from catalog.models import Category, Product


class Command(BaseCommand):
    @staticmethod
    def json_read_products(path):
        # Здесь мы получаем данные из фикстур с продуктами
        with open(path, 'r', encoding='utf-16') as f:
            prod = json.load(f)
        return prod

    def handle(self, *args, **options):
        Product.objects.all().delete()

        prod_path = os.path.abspath('fix_Products.json')
        prod_list = self.json_read_products(prod_path)

        products_for_create = []
        for prod_item in prod_list:
            # prod_item['fields']['category'] = Category.objects.get_or_create(pk=1)
            products_for_create.append(Product(**prod_item['fields']))
        Product.objects.bulk_create(products_for_create)

