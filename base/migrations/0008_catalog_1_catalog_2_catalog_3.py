# Generated by Django 5.0.6 on 2024-08-11 12:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0007_age_rename_categories_book_categories_book_age_range"),
    ]

    operations = [
        migrations.CreateModel(
            name="Catalog_1",
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
                (
                    "books",
                    models.ManyToManyField(
                        blank=True, related_name="catalog1_books", to="base.book"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Catalog_2",
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
                (
                    "books",
                    models.ManyToManyField(
                        blank=True, related_name="catalog2_books", to="base.book"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Catalog_3",
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
                (
                    "books",
                    models.ManyToManyField(
                        blank=True, related_name="catalog3_books", to="base.book"
                    ),
                ),
            ],
        ),
    ]