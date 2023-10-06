from django.shortcuts import render,redirect
from .models import Payment_info
# Create your views here.

def successful(request):
    return render(request, "buynow/successful.html")
    

def buynow(request):
    if request.method=="POST":
        card_no=request.POST["card_no"]
        exp_date=request.POST["exp_date"]
        cvv=request.POST["cvv"]
        name=request.POST["name"]
        print(card_no,exp_date,cvv,name)

        payment_info=Payment_info(card_no=card_no,exp_date=exp_date,cvv=cvv,name=name)
        payment_info.save()

        return redirect('/successful/')    
    return render(request, "buynow/buynow.html")
     