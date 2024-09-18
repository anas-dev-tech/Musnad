# myapp/management/commands/import_products.py

import json
import os
from django.core.management.base import BaseCommand
from product.models import Product, Category

class Command(BaseCommand):
    help = 'Import products from a JSON file into the database'

    
    def handle(self, *args, **kwargs):
        json_file_path = 'sample.json'

        if not os.path.exists(json_file_path):
            self.stdout.write(self.style.ERROR(f'File "{json_file_path}" does not exist.'))
            return

        with open(json_file_path, 'r') as file:
            data = json.load(file)

        products = []
        for item in data:
            # Handle category
            category_name = item.get('category')
            category, created = Category.objects.get_or_create(name=category_name)

            product = Product(
                title=item.get('title'),
                price=item.get('price'),
                description=item.get('description'),
                category=category,
                image=item.get('image'),

            )
            products.append(product)

        # Bulk create products
        Product.objects.bulk_create(products)
        self.stdout.write(self.style.SUCCESS('Successfully imported products.'))