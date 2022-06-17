from django.contrib import admin
from . models import Hobby, User,UserProfile, UserType, Userlog
# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Hobby)
admin.site.register(UserType)
admin.site.register(Userlog)