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
    Cart_total_price =   models.IntegerField()
    Added_at    =   models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Color



class Orders(models.Model):
    user        = models.ForeignKey("User_data", on_delete=models.CASCADE)
    Product     =   models.ForeignKey("Products", on_delete=models.CASCADE)
    Quantity    =   models.IntegerField()
    Color       =   models.CharField(max_length=20)
    Cart_price  =   models.IntegerField()
    Cart_total_price=   models.IntegerField()
    Order_id    =   models.CharField(max_length=50)
    Added_at    =   models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.Order_id



class User_address(models.Model):
    user       = models.ForeignKey("User_data", on_delete=models.CASCADE)
    firstname  = models.CharField(max_length=30)
    lastname   = models.CharField(max_length=30)
    email      = models.EmailField(max_length=30)
    mobile     = models.CharField(max_length=30)
    address    = models.CharField(max_length=100)
    city       = models.CharField(max_length=30)
    state      = models.CharField(max_length=30)
    pincode    = models.IntegerField()
    Added_at   = models.DateTimeField(auto_now_add=True)
    order_id   = models.CharField(max_length=50)

    def __str__(self):
        return self.order_id