from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . models import Hobby, User,UserProfile, UserType, Userlog
# Register your models here.
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'UserProfile':
            kwargs['queryset'] = UserProfile.objects.filter(id=id)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class UserAdmin(BaseUserAdmin):
    inlines = (
            UserProfileInline,
        )

    list_display = ('id', 'username', 'fullname', 'email')
    list_display_links = ('username', 'email','id')
    list_filter = ('username', )
    search_fields = ('username', 'email', )

    fieldsets = (
        ("info", {'fields': ('username', 'password', 'email', 'fullname', 'join_date',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active', )}),)

    filter_horizontal = []

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ( 'join_date', )
        else:
            return ('join_date', )

admin.site.register(User,UserAdmin)
admin.site.register(UserProfile)
admin.site.register(Hobby)
admin.site.register(UserType)
admin.site.register(Userlog)

