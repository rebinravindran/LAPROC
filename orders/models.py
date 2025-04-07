from django.db import models
from customers.models import Customer
from products.models import Product
# Create your models here.
class Orders(models.Model):
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name="orders")

    cart_stage=0
    order_confirm=1
    order_processed=2
    order_delivered=3
    order_rejected=4
    status_order=((order_confirm,"order_confirm"),
                  (order_processed,"order_processed"),
                  (order_delivered,"order_delivered"),
                  (order_rejected,"order_rejected")
                  )
    order_status=models.IntegerField(choices=status_order,default=cart_stage)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)


    class Meta: 
        db_table = 'ordersstatustable'

class Ordereditem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,related_name='added_carts')
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Orders,on_delete=models.CASCADE,related_name='added_items')
    class Meta:
        db_table = 'ordersitemstable'
