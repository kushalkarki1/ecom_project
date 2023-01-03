# Generated by Django 4.1.4 on 2022-12-30 08:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0003_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=4)),
                ('amount_to_be_paid', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
