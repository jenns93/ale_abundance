# Generated by Django 3.2 on 2022-06-16 08:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0012_product_favourites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='favourites',
            field=models.ManyToManyField(blank=True, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
    ]