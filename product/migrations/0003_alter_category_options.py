# Generated by Django 4.1.4 on 2022-12-30 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]