
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('getdata/',views.getdata,name="getdata"),
    # path('getdata/<int:id>/',views.getdata,name="getdata"),
    

]
