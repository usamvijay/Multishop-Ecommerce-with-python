from django.db import models

# Create your models here.

class Categories(models.Model):
    Category_name   =   models.CharField(max_length=50)
    Category_image  =   models.ImageField(upload_to='media/products')
    Created_At      =   models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.Category_name


class Products(models.Model):
    Category        =   models.ForeignKey("Categories", on_delete=models.CASCADE)
    item_name       =   models.CharField(max_length=50)
    item_image      =   models.ImageField(upload_to='media/products',)
    Offer_price     =   models.CharField(max_length=50)
    Original_price  =   models.CharField(max_length=50)
    Quantities      =   models.IntegerField()
    Description     =   models.CharField(max_length=150)
    color           =   models.CharField(max_length=50)
    Added_At        =   models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name



class User_data(models.Model):
    firstname   =   models.CharField( max_length=50)
    lastname    =   models.CharField( max_length=50)
    email       =   models.EmailField()
    mobile      =   models.IntegerField()
    password    =   models.CharField( max_length=50)
    Created_at  =   models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.email


class Cart(models.Model):
    User        =   models.ForeignKey("User_data", on_delete=models.CASCADE)
    Product   =   models.ForeignKey("Products", on_delete=models.CASCADE)
    Quantity    =   models.IntegerField()
    Color       =   models.CharField(max_length=20)
    Cart_price=   models.IntegerField()
    Cart_total_price=   models.IntegerField()
    Added_at    =   models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Color
