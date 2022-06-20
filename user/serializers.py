from rest_framework import serializers
from .models import User as UserModel
from .models import UserProfile as UserProfileModel
from blog.models import Article as ArticleModel
from blog.models import comment as commnetModel
from user.models import Hobby as HobbyModel

class HobbySerializer(serializers.ModelSerializer):
    # serializers.SerializerMethodField()를 사용해 원하는 필드를 생성한다.
    same_hobby_users = serializers.SerializerMethodField()
    def get_same_hobby_users(self, obj):
        print(obj)
        user_list = []
        for user_profile in obj.userprofile_set.all():
            user_list.append(user_profile.user.username)

        return user_list

    class Meta:
        model = HobbyModel
        fields = ["name", "same_hobby_users"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = commnetModel
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    hobby = HobbySerializer(many=True)
    class Meta:
        model = UserProfileModel
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):

    userprofile = UserProfileSerializer()
    article = ArticleSerializer(many=True)
    comment = CommentSerializer(many=True)
    class Meta:
        model = UserModel
        fields = ["username","password","fullname","email","userprofile","article","comment"]
