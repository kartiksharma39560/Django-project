from django.shortcuts import render
from home.models import Product
# Create your views here.

def cart(request):
    products = Product.objects.all()
    params={'product':products}
    return render(request, "cart/cart.html",params)
     