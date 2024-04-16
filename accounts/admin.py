from django.contrib import admin
from .models import Users
from django.contrib.auth.models import Group
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id', 
        'name', 
        'nickname',
        'email',
        'registered_dttm'
        )
    search_fields = ('user_id', 'name', 'nickname', 'email')


admin.site.register(Users, UserAdmin)
admin.site.unregister(Group)