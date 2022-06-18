from django.db import models
from user.models import User

class Category(models.Model):
    category = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Article(models.Model):
    category =models.ManyToManyField(Category)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)

class comment(models.Model):
    title = models.OneToOneField(Article, on_delete=models.CASCADE)
    name = models.OneToOneField(User,on_delete=models.CASCADE)
    desc = models.CharField(max_length=50)
