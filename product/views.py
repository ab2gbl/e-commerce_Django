
from rest_framework import generics
from product.models import *	
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .serializers import *
# Create your views here.

class list_products(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

    
class create_product(generics.CreateAPIView):
    #queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    permission_classes=[IsAdminUser]
    
class edit_product(generics.RetrieveUpdateDestroyAPIView):   
    queryset = Product.objects.all()
    serializer_class = ProductSerializer	
    permission_classes=[IsAdminUser]

class get_product(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    
    	


    
class list_bills(generics.ListCreateAPIView):
    '''{
        "type": "buy",
        "date": "2024-06-09",
        "products": [
            {
                "product": 5 (id),
                "quantity": 2   
            }
        ],
        "price": 1000
    }'''
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    
    permission_classes=[IsAdminUser]
    
    
class create_bills(generics.CreateAPIView):
    '''{
        "type": "buy",
        "date": "2024-06-09",
        "products": [
            {
                "product": 5 (id),
                "quantity": 2   
            }
        ],
        "price": 1000
    }'''
    
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
        
class edit_bills(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    
    
    permission_classes=[IsAdminUser] 

class list_billItems(generics.ListAPIView):
    queryset = BillItem.objects.all()
    serializer_class = BillItemSerializer
    
class edit_billItems(generics.RetrieveUpdateDestroyAPIView):
    queryset = BillItem.objects.all()
    serializer_class = BillItemSerializer
    
    permission_classes=[IsAdminUser] 


class list_sales(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    
    #permission_classes=[IsAdminUser] 