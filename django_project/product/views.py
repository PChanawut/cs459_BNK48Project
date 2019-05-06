from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Product
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm

from .cart import CartItem
import json #change qurry set to json
import pickle
from django.core import serializers

# from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# catagorys = [
#     {
#         'ID': '1',
#         'catagory': 'name1'
#     },
#     {
#         'ID': '2',
#         'catagory': 'name2'
#     },
#     {
#         'ID': '3',
#         'catagory': 'name3'
#     },
# ]


# def register(request):
#     from = UserCreationForm()
#     return base
def my_view(request):
    if request.method == 'POST':
        login(LoginForm(request.POST))
        print(form)

def logout_view(request):
    logout(request)


def product(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        login(LoginForm(request.POST))
    else:
        context = {
            'form': LoginForm(),
            'Categorys': Category.objects.all(),
            'Products': Product.objects.all()
        }
    return render(request, 'category_product.html', context)


def product_type(request, category_type):
    context = {
        'form': LoginForm(),
        'category_types': category_type,
        'Categorys': Category.objects.all(),
        'Products': Product.objects.all()
    }
    return render(request, 'category_type.html', context)


def login_auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        context = {
            'form': LoginForm(),
            'Categorys': Category.objects.all(),
            'Products': Product.objects.all()
        }
        return render(request, 'category_product.html', context)
    else:
        context = {
            'form': LoginForm(),
            'Categorys': Category.objects.all(),
            'Products': Product.objects.all()
        }
        return render(request, 'base_js.html', context)

def add_product(request):
    p_id = request.POST['product_id']
    product_qurry = Product.objects.filter(id = p_id)[0]
    product_json = {
        'id' : product_qurry.id,
        'name' : product_qurry.product_name,
        'price' : product_qurry.product_price,
        'quantity' : 1
    }
    cartItem = CartItem(p_id, 1)
    if 'cart' in request.session:
        cart_session = request.session['cart']
        hasProduct = False
        newTotalPrice = 0
        for cart in cart_session['cartItem'] :
            if product_qurry.id == cart['id'] :
                hasProduct = True
                cart['quantity'] = cart['quantity'] + 1
            newTotalPrice += cart['quantity']*cart['price']
        if not hasProduct :
            cart_session['cartItem'].append(product_json)
            newTotalPrice += product_json['quantity']*product_json['price']
        cart_session['allPrice'] = newTotalPrice 
        request.session['cart'] = cart_session
    else:
        cart_arr = []
        cart_arr.append(product_json)
        # request.session['cart'] = cart_arr
        request.session['cart'] = {
            'allPrice':product_json["price"],
            'cartItem':cart_arr
        }
 
    return redirect('/product') 