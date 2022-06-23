from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    ABV = models.DecimalField(max_digits=6, null=True, decimal_places=2)
    sku = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, blank=False)
    country = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    overall = models.CharField(max_length=6, null=True, blank=False)
    favourites = models.ManyToManyField(
        User, related_name='favourite', blank=True)

    def __str__(self):
        return self.name


class Review_Product(models.Model):
    """
    Review product model
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews_p")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews_u")

    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField()
    
    date_added = models.DateTimeField(auto_now_add=True)

    