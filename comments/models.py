# coding: utf-8
from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from ckeditor.fields import RichTextField


class BaseComment(models.Model):
    content = RichTextField(max_length=1024)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             verbose_name=u'Пользователь')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = u'Базовый комментарий'
        verbose_name_plural = u'Базовые комментарии'
