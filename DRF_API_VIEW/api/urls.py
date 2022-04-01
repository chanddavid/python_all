
from django.urls import path
from api import views

urlpatterns = [
    path('home/',views.StudentAPI.as_view()),
    path('home/<int:id>',views.StudentAPI.as_view()),
    # path('getdata/<int:id>/',views.getdata,name="getdata"),
    

]
