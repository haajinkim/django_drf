from django.db import models
from user.models import User
from datetime import timedelta, timezone , datetime
# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    thumbnail = models.ImageField(upload_to="")
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    show_date = models.DateTimeField(auto_now_add=True)
    end_data = models.DateTimeField(default= datetime.now() + timedelta(days=90), blank=True)     
