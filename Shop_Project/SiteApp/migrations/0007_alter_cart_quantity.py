# Generated by Django 4.1.7 on 2023-02-21 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteApp', '0006_alter_cart_added_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='Quantity',
            field=models.IntegerField(),
        ),
    ]
