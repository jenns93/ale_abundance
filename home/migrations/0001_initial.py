# Generated by Django 3.2 on 2022-06-23 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('issue_type', models.IntegerField(choices=[(0, 'Product'), (1, 'Review'), (2, 'Order'), (3, 'Profile'), (4, 'Other')], default=0)),
                ('issue_details', models.TextField()),
            ],
        ),
    ]