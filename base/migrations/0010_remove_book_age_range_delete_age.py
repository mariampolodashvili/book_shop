# Generated by Django 5.0.6 on 2024-08-14 23:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0009_remove_catalog_2_books_remove_catalog_3_books_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="age_range",
        ),
        migrations.DeleteModel(
            name="Age",
        ),
    ]
