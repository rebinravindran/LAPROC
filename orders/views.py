
from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render,redirect
from app.models import User
from customers.models import Customer
from orders.models import Orders,Ordereditem
from app.views import *
from products.views import *
from django.contrib import messages


# Create your views here.
def cartpage(request):
    user=request.user
    customer=user.customer_profile
    cartobj,created=Orders.objects.get_or_create(
            owner=customer,
            order_status=Orders.cart_stage,
        )
    return render(request,"cart.html",{'cart':cartobj})

def addtocart(request):
    if request.user.is_authenticated:
        if request.POST:
            user=request.user
            customer=user.customer_profile 
            quantity=int(request.POST.get("quantity"))
            prodid=request.POST.get("productid")
            cartobj,created=Orders.objects.get_or_create(
                owner=customer,
                order_status=Orders.cart_stage
            )
    
            product=Product.objects.get(pk=prodid)
            ordered_item,created=Ordereditem.objects.get_or_create(
                product=product,
                owner=cartobj,
        
            ) 
            if created:
                ordered_item.quantity=quantity
                ordered_item.save()

            else:
                ordered_item.quantity=ordered_item.quantity+quantity
                ordered_item.save()
        return redirect(cartpage)
    else:
        return redirect(loging)


def removeitem(request,pk):
    item=Ordereditem.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect("cartpage")



def increment_value(request):
    if request.method == 'POST':
        # Assuming you have a session variable to store the value
        value = request.session.get('increment_value', 0)
        value += 1
        request.session['increment_value'] = value
        return redirect('your_template')
    return render(request, 'your_template.html')


def checkout_cart(request):
    if request.POST:
        if request.POST:
            user=request.user
            customer=user.customer_profile 
            total=float(request.POST.get("total"))
            orderobj=Orders.objects.get(
                owner=customer,
                order_status=Orders.cart_stage
            )
            if orderobj:
                orderobj.order_status=Orders.order_confirm
                orderobj.save()
                statusmessage="your order processed"
                messages.success(request,statusmessage)
            else:
                statusmessage="No items in cart"
                messages.error(request,statusmessage)

        else:
            statusmessage="No items in cart"
            messages.error(request,statusmessage)
    return redirect('cartpage')


# def checkout(request):
#     return render(request,"checkout.html")

def vieworders(request):
    user=request.user
    customer=user.customer_profile 
    allorders=Orders.objects.filter(owner=customer).exclude(order_status=Orders.cart_stage)
    op={'orders':allorders}
    return render(request,'orderstatus.html',op)

import razorpay
from django.views.decorators.csrf import csrf_exempt

import razorpay
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def make_payment(request):
    if request.method == "POST":
        user = request.user
        customer = user.customer_profile
        
        total = float(request.POST.get('total'))  # Get total from cart form
        delivery_charge = 100  # Fixed delivery charge
        total_with_delivery = total + delivery_charge  # Final total amount

        amount = int(total_with_delivery * 100)  # Razorpay needs amount in paise

        client = razorpay.Client(auth=("rzp_test_JAeLcxoJpwFjEq", "PvjOeaEQA5b2gH4XHxEGEhMB"))

        payment = client.order.create({
            'amount': amount,
            'currency': 'INR',
            'payment_capture': '1'
        })

        context = {
            'total': total,
            'payment': payment
        }

        return render(request, 'payment.html', context)

    return redirect('cartpage')

