from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm

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
        # if form.is_valid():
        #     print('get')
        #     HttpResponseRedirect('/thanks/')
        # return render(request, 'product.html', context)
    # else:
    # Return an 'invalid login' error message.
    # ...


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
        # Return an 'invalid login' error message.
        ...
    # context = {
    #     'form': LoginForm(),
    #     'category_types': category_type,
    #     'Categorys': Category.objects.all(),
    #     'Products': Product.objects.all()
    # }
    # return render(request, 'login.html', context)
