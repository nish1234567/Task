from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
class ProductViews(APIView):
    def get(self,request):
        category = self.request.query_params.get('category')
        if category:
            category = Product.objects.filter(category__category_name = category)
        else:
            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset,many=True)
            return Response({'count':len(serializer.data), 'data' : serializer.data})