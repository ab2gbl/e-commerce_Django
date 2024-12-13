# Generated by Django 5.0.2 on 2024-02-27 19:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_remove_product_active_product_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bill_product', to='product.product'),
        ),
    ]
