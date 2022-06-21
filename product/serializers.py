from rest_framework import serializers
from .models import Product
from user.models import User
from django.db.models.query_utils import Q
from django.utils import timezone

class ProductSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    def get_product(self,obj):
        
        Products = Product.objects.filter(id=obj.id).filter(Q(end_data__gte=timezone.now()))
        return [{"title":product.title} for product in Products]


    class Meta:
        model = Product
        fields = ["title","thumbnail","content","end_data","user","product"]
    def validate(self, data):
        return data
    def create(self, validated_data):
        product = Product(**validated_data)
        product.save()
        return product
    # def update(self, validated_data):
    #     product = Product(**validated_data)
    #     product.save()
    #     return product    
class UsergetSerializer(serializers.ModelSerializer):
    product_set = ProductSerializer(many=True)
    class Meta:
        model = User
        fields = ["email","product_set"]

