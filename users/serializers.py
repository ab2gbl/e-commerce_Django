from rest_framework import serializers
from .models import User,Client,Admin
from rest_framework.authtoken.models import Token

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'username', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True},
                        'role': {"read_only": True},}

    def create(self, validated_data):
        user = Client.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'username', 'email', 'password','role','is_staff']
        extra_kwargs = {'password': {'write_only': True},
                        'role': {"read_only": True},
                        'is_staff': {'read_only': True},
                    }

    def create(self, validated_data):
        user = Admin.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            
            is_staff = validated_data.pop('is_staff', True)
        )
        
        return user
    
class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key']
        extra_kwargs = {
                        'key': {'write_only': True},
                        }
    