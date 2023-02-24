from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Categories, Products, User_data, Cart
from SiteApp import models
from six import ensure_binary
from hashlib import md5
from django.contrib import messages

# Create your views here.


def isAlreadyLogin(request):
    if request.session.has_key('User_email') and request.session.has_key('User_role') and request.session.has_key('User_id'):
        return True
    return False


def index(request):
    Category    =   Categories.objects.all()
    Items       =   Products.objects.all()
    return render(request, 'Site/index.html', {'Category':Category, 'Items':Items})


def Shop(request):
    Cate_id     = request.GET.get('category')
    if Cate_id:
        Items       =   Products.objects.filter( Category = Cate_id )
    else:
        Items       =   Products.objects.all()
    return render(request, 'Site/shop.html',{'Items': Items})


def Shop_details(request, id):
    Items   =   Products.objects.filter(id = id)
    return render(request, 'Site/Shop_details.html', {'Items': Items})

def Checkout(request):
    return render(request, 'Site/checkout.html')


def Register(request):
    return render(request, 'Site/Register.html')


def User_Registration(request):
    if request.method =='POST':
        if request.POST['password'] == request.POST['Cpassword']:
            User  = models.User_data()
            if User_data.objects.filter(email = request.POST['email']):
                messages.warning(request, 'Your Email is Alrdedy Existed...')
                return HttpResponseRedirect('/site/Register')
            else:
                User.firstname  =  request.POST['fristname']
                User.lastname   =  request.POST['lastname']
                User.email      =  request.POST['email']
                User.mobile     =  request.POST['mobile']
                User.password   =  md5(ensure_binary(request.POST['password'])).hexdigest()
                User.save()
                return HttpResponseRedirect('/site/index')
        else:
            messages.warning(request, ' Password  & Confirm Password must be same...')
            return HttpResponseRedirect('/site/Register')
    else:
        return HttpResponseRedirect('/site/Register')



def Login_page(request):
    return render(request, 'site/Login.html')



def User_Login(request):
    if isAlreadyLogin(request):
        return HttpResponseRedirect('/site/index')
    else:
        if request.method == 'POST':
            email       = request.POST['email']
            password    =   md5(ensure_binary(request.POST['password'])).hexdigest()
            if models.User_data.objects.filter(email = email, password = password).exists():
                User        =   models.User_data.objects.get(email = email)
                request.session['User_email']   =   email
                request.session['User_role']    =   'User'
                request.session['User_id']      =   User.id
                messages.success(request, 'Youre Logedin Succussefully...!')
                return HttpResponseRedirect('/site/index')
            else:
                messages.success(request, 'Youre Email or Password is Invalid...!')
                return HttpResponseRedirect('/site/Login_page')
        else:
                return HttpResponseRedirect('/site/Login_page')
    return HttpResponseRedirect('/site/index')


def User_logout(request):
    try:
        del request.session['User_email']
        del request.session['User_role']
    except:
        pass
    return HttpResponseRedirect('/site/index')
       

def Cart_page(request):
    if isAlreadyLogin(request):
        User    = User_data.objects.get(email = request.session['User_email'])
        cart = Cart.objects.filter(User = User.id)
        total_price = 0
        for item in cart:
            total_price = total_price + int(item.Cart_price) * int(item.Quantity)
        return render(request, 'Site/cart.html', {'cart':cart, 'total_price':total_price })



def Add_to_Cart(request):
    if isAlreadyLogin(request):
        if request.method =='POST':
            User    = request.session['User_email']
            User    = User_data.objects.get(email = User)
            User_id = User.id
            if Cart.objects.filter(User = User_id, Product = request.POST['product']).exists():
                messages.warning(request, 'This Item has alredy in Cart..')
                return HttpResponseRedirect('/site/Cart')
            else:
                cart    = models.Cart()
                cart.User_id = User_id
                cart.Product_id =   request.POST['product']
                cart.Quantity    =   request.POST['Quantity']
                cart.Color      =   request.POST['color']
                cart.Cart_price =   request.POST['price']
                price           =   request.POST['price']
                Qty             =   request.POST['Quantity']
                cart_total_price= 0
                total_price     =   cart_total_price + int(price) * int(Qty)
                cart.Cart_total_price = total_price
                cart.save()
                messages.info(request,  'Item Added to Cart Successfully..!')
                return HttpResponseRedirect('/site/Cart')
        else:
            return HttpResponseRedirect('/site/Shop_details')
    else:
        return HttpResponseRedirect('/site/User_Login')


def delete_cart_item(request, id):
    if isAlreadyLogin(request):
        Cart_item = Cart.objects.filter( id = id)
        Cart_item.delete()
        messages.success(request,  'Cart Item Is Removed..!')
        return HttpResponseRedirect('/site/Cart')
    else:
        return HttpResponseRedirect('/site/User_Login')
