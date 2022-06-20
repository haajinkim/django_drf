from django.db import models
from user.models import User
from datetime import datetime
from datetime import timedelta

class Category(models.Model):
    category = models.CharField(max_length=50)
    # desc = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Article(models.Model):
    category =models.ManyToManyField(Category, related_name='cateogry')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    start_time = models.DateTimeField(default=datetime.now, blank=True)
    end_time = models.DateTimeField(default= datetime.now() + timedelta(days=90), blank=True)

class comment(models.Model):
    title = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='comment')
    desc = models.CharField(max_length=50)
