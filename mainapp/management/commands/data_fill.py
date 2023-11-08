import json
from django.core.management import BaseCommand
from mainapp.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('category.json', 'r', encoding="utf-8") as file:
            data_category = json.load(file)
            categories_for_create = []
            for category_item in data_category:
                categories_for_create.append(Category(**category_item['fields']))

            Category.objects.all().delete()
            Category.restart_id()
            Category.objects.bulk_create(categories_for_create)


        with (open('product.json', 'r', encoding="utf-8") as file):
            data_product = json.load(file)
            products_for_create = []
            for product_item in data_product:
                product_item['fields']['category'] = Category.objects.get(id= product_item['fields']['category'])
                products_for_create.append(Product(**product_item['fields']))

            Product.objects.all().delete()
            Product.objects.bulk_create(products_for_create)