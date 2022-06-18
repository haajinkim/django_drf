from django.shortcuts import render
from user.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django_drf.permissions import RegistedMoreThanAWeekUser
# Create your views here.

class BlogApiview(APIView):
    permission_classes = [RegistedMoreThanAWeekUser]
    def post(self, request):
        user = request.user
        title = request.data.get('title',"")
        category = request.data.get('category',"")
        desc = request.data.get('desc',"")
        if len(title) <= 5:
            return Response({'게시글을 작성할 수 없습니다!'})
        elif len(desc) <= 20:
            return Response({'댓글을 작성할 수 없습니다!'})
        elif category == "":
            return Response({'카테고리를 지정해야 합니다!'})
        # print(title,cartegory,desc)
        return Response({'저장완료'},status=status.HTTP_200_OK)