from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(Phone)
admin.site.register(Accessory)
admin.site.register(Bill)
admin.site.register(BillItem)


