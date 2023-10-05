from django.shortcuts import render

# Create your views here.

def buynow(request):
    return render(request, "buynow/buynow.html")
     