# Generated by Django 5.0.2 on 2024-02-26 20:33

import product.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=product.models.product_image_path),
        ),
    ]
