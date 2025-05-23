# Generated by Django 5.1.8 on 2025-04-09 09:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("english_name", models.CharField(max_length=200)),
                ("url", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="HistoricalPrice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "discounted_price",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="price_tracker.product",
                    ),
                ),
            ],
        ),
    ]
