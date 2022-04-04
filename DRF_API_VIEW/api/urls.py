
import imp
from django.urls import path,include
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

urlpatterns = [
    path('home/',views.StudentAPI.as_view()),
    path('home/<int:id>',views.StudentAPI.as_view()),
    # path('auth/',include('rest_framework.urls')), #ogin prompt in session auth
    path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh'),
    path('verifytoken/',TokenVerifyView.as_view(),name='token_verify'),
    

]
