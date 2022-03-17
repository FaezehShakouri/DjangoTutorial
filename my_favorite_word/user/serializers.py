from rest_framework import serializers
from .models import CustomUser, Favorite

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'first_name', 'last_name']