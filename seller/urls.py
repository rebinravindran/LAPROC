from django.urls import path
from seller import views



urlpatterns = [

    path("sreg",views.sellerreg,name="sellerreg"),
    path("viewseller",views.viewseller,name="viewseller"),
    path("pendingsellers",views.pendingsellers,name="pendingsellers"),
    path("approve/<id>",views.approve_seller,name="approve_seller"),


    
    path("rejectseller/<id>",views.reject_seller,name="reject_seller"),
    path("removeseller/<id>",views.remove_seller,name="remove_seller"),
    path("sellerpage",views.sellerpage,name="sellerpage"),














    

]