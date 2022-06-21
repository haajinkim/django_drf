from django.shortcuts import render
from user.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django_drf.permissions import RegistedMoreThanAWeekUser, IsAdminOrIsAuthenticatedReadOnly
from blog.serializers import ArticleSerializers
from blog.models import Article , Category
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class BlogApiview(APIView):
    permission_classes = [IsAdminOrIsAuthenticatedReadOnly]
    def get(self,request):
        
        user = request.user
        return Response(ArticleSerializers(user).data)

    # permission_classes = [RegistedMoreThanAWeekUser]
    def post(self, request):
        user = request.user
        title = request.data.get('title',"")
        categorys = request.data.get('category',"")
        desc = request.data.get('desc',"")
        if len(title) <= 5:
            return Response({'게시글을 작성할 수 없습니다!'})
        elif len(desc) <= 20:
            return Response({'댓글을 작성할 수 없습니다!'})
        elif categorys == "":
            return Response({'카테고리를 지정해야 합니다!'})
    
        categroy_objets = []
        for category in categorys:
            category_object,_ = Category.objects.get_or_create(category=category)
            categroy_objets.append(category_object)
            
        new_article = Article.objects.create(
            user = user,
            title = title,
            desc = desc,
        )
        new_article.category.add(*categroy_objets)

        return Response({'저장완료'},status=status.HTTP_200_OK)