from django.urls import path
from app import views

urlpatterns = [
    path("",views.home,name="home"),
    path("home1",views.home1,name="home1"),

    path("logi",views.loging,name="loging"),
    path("admin1",views.admins,name="admins"),
    path('logou',views.logouts,name='logouts'),
    path('invalid',views.invalids,name='invalids'),



    

]