from django.contrib import admin
from .models import Categories,Products,User_data, Cart,User_address,Orders

# Register your models here.
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(User_data)
admin.site.register(Cart)
admin.site.register(Orders)
admin.site.register(User_address)
