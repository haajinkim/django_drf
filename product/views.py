from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from urllib import request
from .models import Product
from .serializers import ProductSerializer
from django.utils import timezone
# Create your views here.
class ProductView(APIView):
    def get(self,request):
        user = request.user
        products = Product.objects.filter(user=user)
        print(products)
        return Response(ProductSerializer(products,many=True).data ,status=status.HTTP_200_OK)
        

        # return Response(ProductSerializer(products,many=True) ,status=status.HTTP_200_OK)
    # def post(self,request):
    #     user = request.user
    #     request.data['user'] = user.id
    #     productserialzier = ProductSerializer(data=request.data)
    #     if productserialzier.is_valid():
    #         productserialzier.save()      
    #         return Response(productserialzier.data, status.HTTP_200_OK)
    #     return Response(productserialzier.errors,status=status.HTTP_400_BAD_REQUEST)
    # def put(self,request,obj_id):
    #     product = Product.objects.get(id=obj_id)
    #     productserialzier = ProductSerializer(product , data = request.data, partial=True)
    #     if productserialzier.is_valid():
    #         productserialzier.save()      
    #         return Response(productserialzier.data, status.HTTP_200_OK)
    #     return Response(productserialzier.errors,status=status.HTTP_400_BAD_REQUEST)