from django.shortcuts import render,redirect
from .models import Product
from django.http import HttpResponse
from math import ceil
# Create your views here.


def productview(request,myid):
    
    
    # Fetch the product using the id
    
    product = Product.objects.filter(id=myid)

     
    return render(request, "home/productview.html", {'product':product[0]} ) 


def productcard(request):
    products = Product.objects.all()
    n = len(products)
    nSlides = n//4 + ceil((n/4) + (n//4))
    params = {'no_of_slides': nSlides, 'range': range(
        1, nSlides), 'product': products}
    return render(request, "home/productcard.html",params)


def home(request):
    products = Product.objects.all()
    n = len(products)
    nSlides = n//4 + ceil((n/4) + (n//4))
    params = {'no_of_slides': nSlides, 'range': range(
        1, nSlides), 'product': products}
    return render(request, "home/homepage.html", params)

def add_to_cart(request):
    # product = Product.objects.filter(id=myid)
    # if request.POST.get('addCart') == 'clicked':

    #     print(products) 
         
    return render(request, "cart/cart.html")
    
       
        
           
        
   


   
