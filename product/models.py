from django.db import models
import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

from django.conf import settings


def product_image_path(instance, filename):
    return os.path.join('upload/products/', instance.name, filename)

class Product (models.Model):
    
    types = [
        ('phone', 'Phone'),
        ('accessory', 'Accessory'),
    ]
    type = models.CharField(max_length=20,choices=types,default='phone',)
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to=product_image_path)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    in_stock =models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=False)
    
    
    def __str__(self):			
        return self.brand + ' ' +self.name
    
    def save(self, *args, **kwargs):
        # Update the 'available' field based on the 'in_stock' value
        self.available = self.in_stock > 0
        super().save(*args, **kwargs)
    
class Phone(models.Model):
    
    product = models.OneToOneField(Product, related_name='phone_product', on_delete=models.CASCADE)		# foreign key
    
    dimensions = models.TextField(blank=True, null=True)
    weight = models.TextField(blank=True, null=True)
    cpu = models.TextField(blank=True, null=True)
    memory = models.TextField(blank=True, null=True)
    ram = models.TextField(blank=True, null=True)
    battery = models.TextField(blank=True, null=True)
    camera = models.TextField(blank=True, null=True)
    os = models.TextField(blank=True, null=True)
    other_details = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.product.brand + ' ' +self.product.name
    
    
class Accessory(models.Model):
    
    product = models.OneToOneField(Product, related_name='accessory_product', on_delete=models.CASCADE)		# foreign key
    
    dimensions = models.TextField(blank=True, null=True)
    weight = models.TextField(blank=True, null=True)
    
    other_details = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.product.brand + ' ' + self.product.name
    
    

class Bill(models.Model):
    
    BILL_TYPE_CHOICES = [
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    ]

    type = models.CharField(max_length=4, choices=BILL_TYPE_CHOICES)
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    products = models.ManyToManyField(Product, through='BillItem')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='bills'
    )

    def __str__(self):
        if self.type == 'sell' and self.user:
            return f"Sale to {self.user.username} - {self.date}"
        return f"{self.get_type_display()} Bill - {self.date}"
    
    
    
class BillItem(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='bill_product' ,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} {self.product.name} in {self.bill.get_type_display()} Bill - {self.bill.date}"
    
    def clean(self):
        if self.bill.type == 'sell' and self.quantity > self.product.in_stock:
            raise ValidationError({'quantity': 'Not enough stock available for the product.'})


    
@receiver(post_save, sender=BillItem)
def update_product_stock(sender, instance, **kwargs):
    if instance.bill.type == 'buy':
            instance.product.in_stock += instance.quantity
            instance.product.save()
    elif instance.bill.type == 'sell':
        instance.product.in_stock -= instance.quantity
        instance.product.save()
