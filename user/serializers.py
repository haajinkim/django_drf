from rest_framework import serializers
from .models import User as UserModel
from .models import UserProfile as UserProfileModel
from blog.models import Article as ArticleModel
from blog.models import comment as commnetModel


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = commnetModel
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    article = ArticleSerializer()
    comment = CommentSerializer()
    class Meta:
        model = UserModel
        fields = ["username","password","fullname","email","userprofile",'article','comment']
