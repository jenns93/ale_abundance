# Generated by Django 3.2 on 2022-06-09 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ABV',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
    ]