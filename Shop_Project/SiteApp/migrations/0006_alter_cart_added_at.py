# Generated by Django 4.1.7 on 2023-02-21 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteApp', '0005_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='Added_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
