# Generated by Django 5.0.2 on 2024-02-26 20:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_phone_battery_phone_camera_phone_cpu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.product'),
        ),
    ]
