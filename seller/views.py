from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from app.models import User
from app.views import *
from seller.models import Seller,Approve_Seller





# Create your views here.






def sellerreg(request):
    if request.method == 'POST':
        em = request.POST['semail']
        mb = request.POST['smobile']
        dd = request.POST['slocation']
        usr = request.POST['sname']
        pwd = request.POST['spassword']
        y=Approve_Seller.objects.create(semail=em,sname=usr,slocation=dd,smobile=mb,password=pwd)
        y.save()
        return redirect("loging")
    else:
        return render(request,"sellerregister.html")
    
def approve_seller(request,id):
    s=Approve_Seller.objects.get(id=id)
    u=User.objects.create_user(username=s.sname,email=s.semail,password=s.password,usertype='seller')
    x=Seller.objects.create(sname=s.sname,smobile=s.smobile,semail=s.semail,slocation=s.slocation,sid=u)
    x.save()
    s.delete()

    return  HttpResponse("APPROVED SELLER")

  

def reject_seller(request,id):
    p=Approve_Seller.objects.get(id=id)
    p.delete()
    return  redirect(pendingsellers)


def remove_seller(request,id):
    p=Seller.objects.get(id=id)
    p.delete()
    return  redirect(viewseller)


def pendingsellers(request):
    s=Approve_Seller.objects.all()
    return render(request,'pendingsellers.html',{'data':s})


def viewseller(request):
    m=Seller.objects.all()
    return render(request,'viewseller.html',{'data':m})


def sellerpage(request):
    return render(request,"sellerpage.html")






  
