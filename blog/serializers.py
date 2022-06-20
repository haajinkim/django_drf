from rest_framework import serializers
from . models import Article as ArticleModel
from datetime import timezone
from django.utils import timezone

now = timezone.localtime()

class ArticleSerializers(serializers.ModelSerializer):
    article = serializers.SerializerMethodField()
    def get_article(self, obj):
        time_table= ArticleModel.objects.filter(end_time__gte=timezone.now())
        if  time_table:
            time_table.order_by('-start_time')
            print(time_table)
            return [{"user":article.user.email,"title":article.title,"start_time":article.start_time,"end_time":article.end_time,"desc":article.desc} for article in obj.article_set.all()]
    
    class Meta: 
        model = ArticleModel()
        fields = ["article"]