# Generated by Django 3.2 on 2022-05-30 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ABV',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='overall',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='stlye',
            field=models.CharField(max_length=50),
        ),
    ]
