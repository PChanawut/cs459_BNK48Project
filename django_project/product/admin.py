from django.contrib import admin
from .models import Category, Product,bill, billItem
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(bill)
admin.site.register(billItem)