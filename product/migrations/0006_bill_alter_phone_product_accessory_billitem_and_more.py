# Generated by Django 5.0.2 on 2024-02-26 21:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_phone_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('buy', 'Buy'), ('sell', 'Sell')], max_length=4)),
                ('date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AlterField(
            model_name='phone',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='phone_product', to='product.product'),
        ),
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dimensions', models.TextField(blank=True, null=True)),
                ('weight', models.TextField(blank=True, null=True)),
                ('other_details', models.TextField(blank=True, null=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='accessory_product', to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='BillItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.bill')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='products',
            field=models.ManyToManyField(through='product.BillItem', to='product.product'),
        ),
    ]
