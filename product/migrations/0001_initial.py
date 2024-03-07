# Generated by Django 5.0.3 on 2024-03-07 11:02

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AccessoriesType",
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
                    "public_id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("name", models.CharField(max_length=256)),
                ("slug", models.SlugField(max_length=300, unique=True)),
                ("description", models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Brand",
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
                    "public_id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("name", models.CharField(max_length=200)),
                ("slug", models.SlugField(max_length=300, unique=True)),
                ("description", models.CharField(max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Category",
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
                    "public_id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("name", models.CharField(max_length=200)),
                ("slug", models.SlugField(max_length=300, unique=True)),
                ("description", models.CharField(max_length=2000, null=True)),
            ],
        ),
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
                (
                    "public_id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("name", models.CharField(max_length=255)),
                ("title", models.CharField(max_length=1000, null=True)),
                ("slug", models.SlugField(blank=True, unique=True)),
                ("quantity", models.PositiveIntegerField(default=0)),
                (
                    "discount",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                ("size", models.CharField(max_length=32, null=True)),
                ("is_publish", models.BooleanField(default=False)),
                (
                    "thumbnail_image",
                    models.ImageField(upload_to="products/thumbnail_images"),
                ),
                ("description", models.TextField()),
                (
                    "price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "accessory_type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="product_types",
                        to="product.accessoriestype",
                    ),
                ),
                (
                    "brand",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="products",
                        to="product.brand",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductHaveColor",
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
                ("name", models.CharField(max_length=32)),
                (
                    "product",
                    models.ManyToManyField(
                        related_name="product_color", to="product.product"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductHaveImages",
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
                    "public_id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("image", models.ImageField(upload_to="products/images")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_images",
                        to="product.product",
                    ),
                ),
            ],
        ),
    ]