#coding:  utf-8
from django.contrib import admin

from .models import BaseComment


class BaseCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'content_type',)

admin.site.register(BaseComment, BaseCommentAdmin)
