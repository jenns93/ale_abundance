# Generated by Django 3.2 on 2022-06-23 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_auto_20220623_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ABV',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='overall',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True),
        ),
    ]