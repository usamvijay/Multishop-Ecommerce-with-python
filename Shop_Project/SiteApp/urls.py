
from django.contrib import admin
from django.urls import path
from SiteApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('Shop/', views.Shop, name='Shop'),
    path('Shop_details/<int:id>/', views.Shop_details, name='Shop_details'),
    path('Shop_details/', views.Shop_details, name='Shop_details'),
    path('Checkout/', views.Checkout, name='Checkout'),
    path('Register/', views.Register, name='Register'),
    path('User_Registration/', views.User_Registration, name='User_Registration'),
    path('Login_page/', views.Login_page, name='Login_page'),
    path('User_Login/', views.User_Login, name='User_Login'),
    path('User_logout/', views.User_logout, name='User_logout'),
    path('Cart/', views.Cart_page, name='Cart_page'),
    path('Add_to_Cart/', views.Add_to_Cart, name='Add_to_Cart'),
    path('delete_cart_item/<int:id>/', views.delete_cart_item, name='delete_cart_item'),
    path('Add_User_address/', views.Add_User_address, name="Add_User_address")
]
