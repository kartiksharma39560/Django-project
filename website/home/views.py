from django.shortcuts import render, redirect
from .models import Product
from .models import Signup
from django.http import HttpResponse, JsonResponse
from math import ceil
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as dj_login , logout 
from django.contrib import messages
# Create your views here.


def productview(request, myid):
    products = Product.objects.all()
    # Fetch the product using the id
    n = len(products)
    nSlides = n//4 + ceil((n/4) + (n//4))
    product = Product.objects.filter(id=myid)
    params = {'no_of_slides': nSlides, 'range': range( 1, nSlides), 'product': products, }
                                                
    return render(request, "home/productview.html",{'product': product[0]} )


def productcard(request):
    products = Product.objects.all()
    n = len(products)
    nSlides = n//4 + ceil((n/4) + (n//4))
    params = {'no_of_slides': nSlides, 'range': range(
        1, nSlides), 'product': products}
    return render(request, "home/productcard.html", params)


def home(request):
    products = Product.objects.all()
    n = len(products)
    nSlides = n//4 + ceil((n/4) + (n//4))
    params = {'no_of_slides': nSlides, 'range': range(
        1, nSlides), 'product': products}
    return render(request, "home/homepage.html", params)


def updateItem(request):
   return render(request, "home/base.html")

def signupage(request):
    if request.method == 'POST':
        uname= request.POST.get('username')
        email=request.POST.get('email')
        p1=request.POST.get('password1')
        p2=request.POST.get('password2')
        
        if p1!=p2:
            return HttpResponse("PASSWORD NOT SAME ")
        my_user=User.objects.create_user(uname,email,p1)
        my_user.save()
        sign=Signup(uname=uname,email=email,p1=p1)
        sign.save()
        return redirect('login')
     
    return render(request, "home/signup.html")



 

def login(request):
    if request.method == 'POST':
        usname = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=usname, password=pass1)
        if user is not None:
            dj_login(request, user)
            return redirect('home')
        else:
            # Use Django messages framework to store and retrieve the error message
            return HttpResponse(request, 'Username or password is incorrect')
    
    return render(request, "home/login.html")




def Logoutpage(request):
    logout(request)
    return redirect('login')