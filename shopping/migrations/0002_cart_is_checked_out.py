# Generated by Django 4.1.4 on 2022-12-30 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='is_checked_out',
            field=models.BooleanField(default=False),
        ),
    ]