from unittest import result
from urllib import request
from django.shortcuts import render
from . models import User, Userlog
from blog.models import Article
from django.contrib.auth import login, authenticate, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from rest_framework import serializers
from django.core import serializers
from user.serializers import UserSerializer, ArticleSerializer
import datetime as dt
# Create your views here.


class Join_Apiview(APIView):
    # permission_classes = [permissions.AllowAny]
    def post(self, request):
        email = request.data.get('email','')
        password = request.data.get('password', "")
        user_type = request.data.get('user_type', "")
        user_find = User.objects.filter(email=email)
        if user_find:
        # user_log_find = Userlog.objects.filter(email=email)
        # if not user_find:
            return Response({'message': '가입 실패!'})
        else:
            user = User(
            email = email,
            password = password,
            )
            user.save()
            return Response({'message': '가입 성공!'})


class UserApiview(APIView):
    # permission_classes = [permissions.AllowAny]
    def get(self, request, id=None):
        user = request.user
        # print(user)
        # serialized_user_data =UserSerializer(user).data

        # print(serialized_user_data)
        # all = Article.objects.filter(id=1)
        # # all = Article.objects.filter(id=user)\
        # titles = []
        # for title in all:
        #     # print(title.title)
        #     titles.append(title)
        #     print(titles[0].title)
        #     user_title = serializers.serialize('json', titles)

        return Response(UserSerializer(user).data)

    def post(self, request): 
        email = request.data.get('email', '') 
        password = request.data.get('password', '')
        user = authenticate(request, email= email, password = password) 
        if not user: 
            return Response({'error' : '존재하지 않는 계정이거나 패스워드가 일치하지 않습니다.'}, status= status.HTTP_401_UNAUTHORIZED) 
        login(request, user) 
        user = request.user
        # Userlog.objects.filter(username=user)
        # for user_data in user_datas:
            # user_log = user_data.login_date
        now_time = dt.datetime.now()
        Userlog.objects.create(user=user, login_date=now_time)
        # .filter(login_date__contains=user).update(
        #     login_date = now_time
        # )

        return Response({'message': '로그인 성공!'}, status=status.HTTP_200_OK) 

    def delete(self, request): 
        logout(request) 
        return Response({'message' : '로그아웃 성공!'}, status=status.HTTP_200_OK)


