from django.urls import path
from customers import views

urlpatterns = [
    path("viewcustomerss",views.viewcustomer,name="viewcustomer"),
    path("reg",views.register,name="register"),
    path("removecustomer/<id>",views.removecustomer,name="removecustomer"),

    path('edcus',views.editcustomer,name='editcustomer'),
    path('upcus',views.updatecustomer,name='updatecustomer'),
    




    

]