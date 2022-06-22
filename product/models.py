from django.db import models
from user.models import User
# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    thumbnail = models.ImageField(upload_to="")
    description = models.TextField()
    price = models.IntegerField()
    create_start = models.DateTimeField(auto_now_add=True)
    edit_date =models.DateTimeField(auto_now=True)
    exposure_end = models.DateTimeField()     
    is_active = models.BooleanField(default=True)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField()
    star_avg = models.FloatField()
    create_date =models.DateTimeField(auto_now_add=True)
