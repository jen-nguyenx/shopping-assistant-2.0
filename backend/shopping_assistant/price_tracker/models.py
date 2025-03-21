from django.db import models


class Product(models.Model):
    english_name = models.CharField(max_length=200)
    url = models.URLField()


class HistoricalPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    full_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
