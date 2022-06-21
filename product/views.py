from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from urllib import request
from .models import Product
from product.serializers import UsergetSerializer, ProductSerializer

# Create your views here.
class ProductView(APIView):
    def get(self,request):
        user = request.user
        return Response(UsergetSerializer(user).data, status=status.HTTP_200_OK)
    def post(self,request):
        user = request.user
        request.data['user'] = user.id
        print(request.data)
        productserialzier = ProductSerializer(data=request.data)
        if productserialzier.is_valid():
            productserialzier.save()      
            return Response({"message": "정상"}, status=status.HTTP_200_OK)
        return Response(productserialzier.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,obj_id):
        user = Product.objects.get(id=obj_id)
        print(user)
        productserialzier = ProductSerializer(user, data=request.data)
        if productserialzier.is_valid():
            productserialzier.save()      
            return Response({"message": "정상"}, status=status.HTTP_200_OK)
        return Response({"message": "정상"})