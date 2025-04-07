from django.urls import path
from products import views


urlpatterns = [
    path("additemss",views.addproducts,name="addproducts"),
    path('viewitemss',views.viewitems,name='viewitems'),
    path('deleteitemss/<int:tt>',views.deleteitems,name='deleteitems'),
    path('edititemss/<int:oo>',views.edititems,name='edititems'),
    path("updateitemss/<int:ap>",views.updateitems,name='updateitems'),
    path("allprod",views.allproducts,name="allproducts"),
    path("allprod1",views.allproducts1,name="allproducts1"),

    
    path("desc/<int:pk>",views.description,name="description"),

    
    path("additemssseller",views.addproductsseller,name="addproductsseller"),
    path("viewitemssseller",views.viewitemsseller,name="viewitemsseller"),

    
    path("search_results",views.search_results,name="search_results"),
    path('filter_by_category/<str:category>/',views.filter_by_category,name="filter_by_category"),


    



    








    

]