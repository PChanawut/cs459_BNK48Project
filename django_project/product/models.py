from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils.timezone import now

class Category(models.Model):
    city_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

    def get_ID(self):
        return self.city_id


class Product(models.Model):
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=30)
    product_image = models.ImageField(upload_to='static/product_list/',
                                      blank=True,
                                      null=True)
    product_price = models.PositiveIntegerField()
    product_active = models.BooleanField(default=True)
    product_description = models.TextField(max_length=500,
                                           blank=True,
                                           null=True)
    product_quatity = models.PositiveIntegerField()

    def __str__(self):
        return self.product_name

class bill(models.Model):
    bill_id = models.AutoField(primary_key=True)
    bill_date = models.DateTimeField(default=now, blank=True)
    bill_userbuy = models.ForeignKey(User, on_delete=models.CASCADE)
    bill_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    bill_quatity = models.IntegerField(default=1)   