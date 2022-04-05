from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.home,name="home"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('details/<int:id>/',views.customerdetail,name='details'),
    path('product/',views.product,name="product"),
    path('updateorder/<int:id>/',views.updateorder,name='updateorder'),
    path('deleteorder/<int:id>',views.deleteorder,name='deleteorder'),
    path('register/',views.registerform,name='register'),
    path('login/',views.loginform,name='login'),
    path('logout/',views.logoutform,name='logout'),
]
