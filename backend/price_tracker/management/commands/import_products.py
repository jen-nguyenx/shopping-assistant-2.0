from django.core.management.base import BaseCommand
from price_tracker.price_scraper import extract_product_name
from price_tracker.models import Product


class Command(BaseCommand):
    help = "Bulk extract product names from provided URL and write to the Product table"

    def add_arguments(self, parser):
        parser.add_argument(
            "file_path", type=str, help="Path to the text file with urls"
        )
        return super().add_arguments(parser)

    def handle(self, *args, **options):
        file_path = options["file_path"]

        try:
            with open(file_path, "r") as file:
                urls = [line.strip() for line in file if line.strip()]

        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"File not found: {file_path}"))
            return

        try:
            for url in urls:
                product_name = extract_product_name(url)
                product_name, created = Product.objects.get_or_create(
                    url=url, defaults={"name": product_name}
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Added: {product_name}"))
                else:
                    self.stdout.write(self.style.WARNING(f"Already exists: {url}"))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Failed to import {url}: {str(e)}"))
