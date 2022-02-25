from dataclasses import field
from rest_framework import serializers
from .models import *

class CartItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = "__all__" 
