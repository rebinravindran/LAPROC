from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from app.models import User
from customers.models import Customer
from app.views import *
from products.views import *



# Create your views here.

def register(request):
    if request.method == 'POST':
        em = request.POST['email']
        mb = request.POST['mobile']
        usr = request.POST['username']
        pwd = request.POST['password']
        y=User.objects.create_user(email=em,username=usr,password=pwd,usertype="customer")
        Customer.objects.create(name=usr,mobile=mb,email=em,usertype="customer",cid=y)
        
        return redirect(loging)
    else:
        return render(request,'register.html')
    


def viewcustomer(request):   
    p=Customer.objects.all()
    return render(request,'viewcustomer.html',{'data':p})

def removecustomer(request,id):
    p=Customer.objects.get(id=id)
    c=User.objects.get(id=id)
    p.delete()
    c.delete()
    return  redirect(viewcustomer)




def editcustomer(request):
    ss=request.session['cus_id']

    us=User.objects.get(id=ss)
    st=Customer.objects.get(cid=ss)
    return render(request,'editprofile.html',{'cust':st,'use':us})

def updatecustomer(request):
    if request.method=='POST':
        ss=request.session['cus_id']

        aa=request.POST['naam']
        cc=request.POST['mobi']
        bb=request.POST['email']

        cid=request.POST['cusid']
    
        # usr=request.POST['username']
        # print(usr)
        m=User.objects.get(id=ss)
        x=Customer.objects.get(cid=ss)
        x.name=aa
        x.email=bb
        x.mobile=cc
        m.username=aa
        m.email=bb
        x.save()
        m.save()
        return redirect(home1)
    