from django.db import models


# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True)


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=128, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_img', blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)




