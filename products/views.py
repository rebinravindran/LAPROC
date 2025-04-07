from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from app.models import User
from products.models import Product
from app.views import *




# Create your views here.


def addproducts(request):
    if request.method == 'POST':
        br = request.POST['Brand']
        pro = request.POST['Product']
        mod = request.POST['Model']
        feat = request.POST['features']
        cat = request.POST["Category"]
        pri = request.POST['price']
        stk= request.POST['stock']
        img = request.FILES['image']


        d=Product.objects.create(brand_name=br,product_name=pro,model_name=mod,Features=feat,category=cat,price=pri,stocks=stk,image=img)
        d.save()
        
        return redirect(addproducts)
    else:
        return render(request,'additems.html')
    

def addproductsseller(request):
    if request.method == 'POST':
        br = request.POST['Brand']
        pro = request.POST['Product']
        mod = request.POST['Model']
        feat = request.POST['features']
        cat = request.POST["Category"]
        pri = request.POST['price']
        stk= request.POST['stock']
        img = request.FILES['image']


        d=Product.objects.create(brand_name=br,product_name=pro,model_name=mod,Features=feat,category=cat,price=pri,stocks=stk,image=img)
        d.save()
        
        return redirect(addproducts)
    else:
        return render(request,'additemsseller.html')
    
def viewitems(request):   
    p=Product.objects.all()
    return render(request,'viewitems.html',{'data':p})

def viewitemsseller(request):   
    p=Product.objects.all()
    return render(request,'viewitemsseller.html',{'data':p})


def deleteitems(request,tt):
    m= Product.objects.get(id=tt)
    m.delete()
    return redirect(viewitems)


def edititems(request,oo):
    m= Product.objects.get(id=oo)
    return render(request,'edititems.html',{'data':m})

def updateitems(request,ap):
    if request.method =='POST':
        aa=request.POST['brand']
        bb=request.POST['product']
        cc=request.POST['model']
        dd=request.POST['feature']
        ee=request.POST['category']
        ff=request.POST["price"]
        gg=request.POST["stock"]
        hh=request.FILES["image"]
        x=Product.objects.get(id=ap)       
        x.brand_name=aa
        x.product_name=bb
        x.model_name=cc
        x.Features=dd
        x.category=ee
        x.price=ff
        x.stocks=gg
        x.image=hh     
        x.save()
        return redirect(viewitems)


def allproducts(request):
    x=Product.objects.all()
    return render(request,"product.html",{'data':x})

def allproducts1(request):
    x=Product.objects.all()
    return render(request,"allproducts.html",{'data':x})



def filter_by_category(request, category):
    results = Product.objects.filter(category=category)
    return render(request, 'filter_by_category.html', {'results': results, 'selected_category': category})


def description(request,pk):
    prod= Product.objects.get(pk=pk)   
    context={'product':prod}    
    return render(request,'description.html',context)


def search_results(request):
    query = request.GET.get('query')
    results = Product.objects.filter(product_name__icontains=query) if query else []
    return render(request, 'search_results.html', {'results': results, 'query': query})
