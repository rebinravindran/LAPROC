from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from app.models import User
from customers.models import Customer
from products.models import Product
from seller.models import Seller,Approve_Seller
from seller.views import *
from products.views import *







def home(request):
    newproducts=Product.objects.order_by('-id')[:5]
    topselling=Product.objects.order_by('id')[:3]
    data={
        'newproducts':newproducts,
        'topselling':topselling
    }
    return render(request,"index.html",data)

def home1(request):
    newproducts=Product.objects.order_by('-id')[:5]
    topselling=Product.objects.order_by('id')[:3]
    data={
        'newproducts':newproducts,
        'topselling':topselling
    }
    return render(request,"index1.html",data)


def admins(request):
    return render(request,"admin.html")


def invalids(request):
    return render(request,"invalid.html")


def loging(request):
    if request.method == 'POST':
        usr= request.POST['username']       
        pwd=request.POST['password']
        user = authenticate(request,username=usr,password=pwd)
        if user is not None and user.is_superuser == 1:
            return redirect(admins)
        elif user is not None and user.usertype=='customer':
            login(request,user)
            cust = Customer.objects.get(cid = user.id)
            request.session['cus_id']=cust.cid.id

            return redirect(home1)
        elif user is not None and user.usertype=='seller':
            login(request,user)
            sell = Seller.objects.get(sid = user.id)
            # request.session['cus_id']=cust.cid.id

            return redirect(sellerpage)
        else:
            return redirect(invalids)
    else:
        return render(request,'login.html')


def logouts(request):
    logout(request)
    return redirect(home)   

