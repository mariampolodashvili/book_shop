# Generated by Django 5.0.6 on 2024-08-11 12:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0008_catalog_1_catalog_2_catalog_3"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="catalog_2",
            name="books",
        ),
        migrations.RemoveField(
            model_name="catalog_3",
            name="books",
        ),
        migrations.DeleteModel(
            name="Catalog_1",
        ),
        migrations.DeleteModel(
            name="Catalog_2",
        ),
        migrations.DeleteModel(
            name="Catalog_3",
        ),
    ]
