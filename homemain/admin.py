from django.contrib import admin
from board.models import NoticeBoardPost,Comment


# Register your models here.

admin.site.register(NoticeBoardPost)
admin.site.register(Comment)