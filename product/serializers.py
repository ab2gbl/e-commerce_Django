from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    details = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id','type', 'brand', 'name', 'image', 'price','in_stock', 'available', 'details']

    def get_details(self, instance):
        if instance.type == 'phone':
            return ProductPhoneSerializer(instance.phone_product).data
        elif instance.type == 'accessory':
            return ProductAccessorySerializer(instance.accessory_product).data
        else:
            return None

        
class ProductPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['dimensions','weight','cpu','memory','ram','battery','camera','os','other_details']
        
class ProductAccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessory
        fields = '__all__'
        

class CreateProductSerializer(serializers.ModelSerializer):
    types = [
        ('phone', 'Phone'),
        ('accessory', 'Accessory'),
    ]
    #type = serializers.CharField(max_length=20,choices=types,default='phone',write_only=True)
    type = serializers.ChoiceField(choices=types,default='phone',write_only=True)
    brand = serializers.CharField(max_length=50,write_only=True)
    name = serializers.CharField(max_length=200,write_only=True)
    image = serializers.ImageField(write_only=True)
    price = serializers.DecimalField(max_digits=6, decimal_places=3,write_only=True)

    class Meta:
        model = Phone 
        fields = ['type','brand', 'name', 'image', 'price','dimensions', 'weight', 'cpu', 'memory', 'ram', 'battery', 'camera', 'os', 'other_details']
    

    
    def create(self, validated_data):
        # Extract phone-specific data
        type = validated_data.pop('type', 'phone')
        dimensions = validated_data.pop('dimensions', None)
        weight = validated_data.pop('weight', None)
        cpu = validated_data.pop('cpu', None)
        memory = validated_data.pop('memory', None)
        ram = validated_data.pop('ram', None)
        battery = validated_data.pop('battery', None)
        camera = validated_data.pop('camera', None)
        os = validated_data.pop('os', None)
        other_details = validated_data.pop('other_details', None)

        # Extract product-specific data
        brand = validated_data.pop('brand')
        name = validated_data.pop('name')
        image = validated_data.pop('image')
        price = validated_data.pop('price')

        # Create a Product instance
        product = Product.objects.create(
            type=type,
            brand=brand,
            name=name,
            image=image,
            price=price
        )
        if type=='phone':
        # Create a Phone instance associated with the created Product
            phone = Phone.objects.create(
                product=product,
                dimensions=dimensions,
                weight=weight,
                cpu=cpu,
                memory=memory,
                ram=ram,
                battery=battery,
                camera=camera,
                os=os,
                other_details=other_details
            )
        elif type=='accessory':
            phone = Accessory.objects.create(
                product=product,
                dimensions=dimensions,
                weight=weight,
                other_details=other_details
            )
        else :
            raise serializers.ValidationError("this type of products does not exist")
        

        return phone 



class BillItemSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    class Meta:
        model = BillItem
        fields = ['product','quantity']
        
    def get_product(self,instance):
        return {'id':instance.product.id,'brand': instance.product.brand, 'name': instance.product.name}
        
    


class CreateBillItemSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='bill_product')
    
    quantity = serializers.IntegerField()
    
    class Meta:
        model = BillItem
        fields = ['product','quantity']

class BillSerializer(serializers.ModelSerializer):
    products = CreateBillItemSerializer(many=True,write_only=True)
    products_details = serializers.SerializerMethodField()

    class Meta:
        model = Bill
        fields = ['id','type', 'date', 'products', 'price','products_details']
        
    def get_products_details(self, instance):
        bill_items = instance.billitem_set.all()  
        return BillItemSerializer(bill_items, many=True).data

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        bill = Bill.objects.create(**validated_data)
        for product_data in products_data:
            
            
            product = product_data['bill_product']
            quantity = product_data['quantity']
            
            BillItem.objects.create(bill=bill, product=product, quantity=quantity)

        return bill


class SaleSerializer(serializers.ModelSerializer):
    paid=serializers.BooleanField(read_only=True)

    class Meta:
        model = Sale
        fields = ['id','user','product','quantity','date','paid']