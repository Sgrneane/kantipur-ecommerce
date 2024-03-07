# Generated by Django 5.0.3 on 2024-03-07 11:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accessoriestype",
            name="slug",
            field=models.SlugField(blank=True, max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name="brand",
            name="slug",
            field=models.SlugField(blank=True, max_length=300, unique=True),
        ),
    ]
