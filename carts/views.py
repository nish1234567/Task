from django.shortcuts import render
from numpy import delete
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
# Create your views here.
class CartViews(APIView):
    def get(self, request):
        Permission_classes = [IsAuthenticated]
        user = user.request
        cart = Cart.objects.filter(user=user,ordered=False).first
        queryset = CartItems.objects.filter(cart = cart) 
        serializer = CartItemsSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        user = request.user
        cart = Cart.objects.get_or_create(user=user,ordered=False)
        product = Product.get.id(id=data.get('product'))
        price = product.price
        quantity = data.get('quantity')
        cart_items = CartItems(cart=cart,user=user,product=product,price=price,quantity=quantity)
        cart_items.save()
        total_price = 0
        cart_items = CartItems.objects.filter(user=user,cart=cart.id)
        for items in cart_items:
            total_price += items.price
        cart.total_price = total_price
        cart.savr()
        return Response({'Success':'Items added to your cart'})

    def put(self,request):
        data = request.data
        cart_items = CartItems.objects.get(id=data.get('id'))
        quantity = data.get('quantity')
        cart_items.quantity+=quantity
        cart_items.save()
        return Response({'Success':'Updated'})

    def delete(self,request):
        user = request.user
        data = request.data
        cart_items = CartItems.objects.get(id=data.get('id'))
        cart_items.delete()
        cart = Cart.objects.filter(user=user, ordered= False).first
        queryset = CartItems.objects.filter(cart=cart)
        serializer = CartItemsSerializer(queryset,many=True)
        return Response(serializer.data)
