# Generated by Django 3.2 on 2022-06-23 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_alter_product_abv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='overall',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
    ]
