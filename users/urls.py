from . import views
from django.urls import path

from rest_framework_simplejwt.views import ( TokenObtainPairView,TokenRefreshView,TokenVerifyView )



urlpatterns = [
	path('client/', views.createClient.as_view()),
	path('admin/', views.createAdmin.as_view()),
	path('users/', views.listUsers.as_view()),
	path('myinfo/', views.myInfo.as_view()),
  
	
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('token/verify/', TokenVerifyView.as_view(), name='token_verify')
 
]