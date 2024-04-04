
from rest_framework import generics
from product.models import *	

from .serializers import *
# Create your views here.

class list_products(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

    
class create_product(generics.CreateAPIView):
    #queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    
class edit_product(generics.RetrieveUpdateDestroyAPIView):   
    queryset = Product.objects.all()
    serializer_class = ProductSerializer		


    
class list_bills(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
        
class edit_bills(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class list_billItems(generics.ListAPIView):
    queryset = BillItem.objects.all()
    serializer_class = BillItemSerializer
    
class edit_billItems(generics.RetrieveUpdateDestroyAPIView):
    queryset = BillItem.objects.all()
    serializer_class = BillItemSerializer


class list_sales(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer