from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Product
from user.models import Hobby, User,UserProfile, UserType, Userlog
# Register your models here.


admin.site.register(Product)