# Generated by Django 4.1.7 on 2023-02-20 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(max_length=50)),
                ('Category_image', models.ImageField(upload_to='media/products')),
                ('Created_At', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
