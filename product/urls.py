from . import views
from django.urls import path
urlpatterns = [
	path('products/', views.list_products.as_view()),
	path('create/', views.create_product.as_view()),
  	path('product/<int:pk>', views.edit_product.as_view()),
	path('bills/', views.list_bills.as_view()),
	path('createbills/', views.create_bills.as_view()),
 
  	#path('bill/<int:pk>', views.edit_bills.as_view()),
	#path('createbill/', views.create_bill.as_view()),
 	path('billitems/', views.list_billItems.as_view()),
  	#path('billitem/<int:pk>', views.edit_billItems.as_view()),
   	path('sales/', views.list_sales.as_view()),

	

 
]