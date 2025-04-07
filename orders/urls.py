from django.urls import path
from orders import views

urlpatterns = [
    path("cart",views.cartpage,name="cartpage"),
    path("addtocart",views.addtocart,name="addtocart"),
    path("removeitem/<pk>",views.removeitem,name="removeitem"),
    path('plus',views.increment_value,name='increment_value'),
    path('checkout',views.checkout_cart,name='checkout_cart'),
    path('vieworders',views.vieworders,name='vieworders'),


    



    




]  
