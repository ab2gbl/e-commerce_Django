from users.serializers import *
from rest_framework import generics
from product.models import *	
from .models import *
from rest_framework.permissions import IsAdminUser,IsAuthenticated
# Create your views here.
class createClient(generics.CreateAPIView):
    queryset = Client.objects.filter(role=User.Role.CLIENT)
    serializer_class = ClientSerializer
    
    
class createAdmin(generics.CreateAPIView):
    queryset = Admin.objects.filter(role=User.Role.ADMIN)
    serializer_class = AdminSerializer
    permission_classes=[IsAdminUser]
    
class listUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = ClientSerializer
    permission_classes=[IsAdminUser]
    
class myInfo(generics.RetrieveAPIView):
    serializer_class = ClientSerializer
    def get_object(self):
        return self.request.user
    
    permission_classes=[IsAuthenticated]
    