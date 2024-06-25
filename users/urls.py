from . import views
from django.urls import path
urlpatterns = [
	path('client/', views.createClient.as_view()),
	path('admin/', views.createAdmin.as_view()),
	path('users/', views.listUsers.as_view()),
	path('myinfo/', views.myInfo.as_view()),
 
]