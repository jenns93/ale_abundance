from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    
    ABV = models.CharField(max_length=6, null=True, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    overall = models.CharField(max_length=50, null=True, blank=True)
    

    def __str__(self):
        return self.name