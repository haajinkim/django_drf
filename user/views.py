from unittest import result
from urllib import request
from django.shortcuts import render
from . models import User
from blog.models import Article
from django.contrib.auth import login, authenticate, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from rest_framework import serializers
from django.core import serializers
# Create your views here.



class UserApiview(APIView):
    # permission_classes = [permissions.AllowAny]
    def get(self, request):
        user = request.user
        all = Article.objects.filter(id=1)
        # all = Article.objects.filter(id=user)\
        titles = []
        for title in all:
            # print(title.title)
            titles.append(title)
            print(titles[0].title)
            user_title = serializers.serialize('json', titles)

        return Response({'message': '전송 성공!',"user_title":user_title})

    def post(self, request): 
        username = request.data.get('username', '') 
        password = request.data.get('password', '') 
        user = authenticate(request, username= username, password = password) 
        print(user)
        if not user: 
            return Response({'error' : '존재하지 않는 계정이거나 패스워드가 일치하지 않습니다.'}, status= status.HTTP_401_UNAUTHORIZED) 
        
        login(request, user) 
        return Response({'message': '로그인 성공!'}, status=status.HTTP_200_OK) 

    def delete(self, request): 
        logout(request) 
        return Response({'message' : '로그아웃 성공!'}, status=status.HTTP_200_OK)


