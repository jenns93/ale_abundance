# Generated by Django 3.2 on 2022-06-23 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_alter_product_abv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='overall',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
