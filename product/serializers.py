from rest_framework import serializers
from .models import Product, Review
from user.models import User
from datetime import timezone

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["description","star_avg","create_date"]


class ProductSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True)
    # reviews = serializers.SerializerMethodField()
    # def get_reviews(self,obj):
    #     print(obj)
    #     print(dir(obj.review_set))
    #     return "test"
    class Meta:
        model = Product
        fields = ["review_set","user","title","thumbnail","description","price",
        "create_start","edit_date","exposure_end"]
    def validate(self, data):
        # product = Product.objects.get(id=obj_id)
        if data.get('exposure_end') >= timezone.now():
            return data
    def create(self, validated_data):
        get_desc_data =  validated_data.pop("description") + str(timezone.now()) +  "에 수정된 게시물입니다." 
        product = validated_data['description'] = get_desc_data
        product = Product(**validated_data)

        product.save()
        return product
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == 'description':
                value = str(timezone.now()) +"에 수정된 게시물입니다" + value
            setattr(instance, key, value)
        instance.save()
        return instance



