from django.db import models


class Product(models.Model):
    english_name = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.english_name


class HistoricalPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    full_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.english_name + self.timestamp}"


class Brand(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
