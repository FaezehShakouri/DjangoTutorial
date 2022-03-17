from rest_framework import serializers
from user.models import Favorite, CustomUser


class FavoriteSerializer(serializers.ModelSerializer):
    # weight = serializers.ReadOnlyField()
    
    class Meta:
        model = Favorite
        fields = ['id', 'word', 'weight']

class CustomUserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'favorites']
        depth = 1

