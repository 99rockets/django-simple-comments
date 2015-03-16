#coding: utf-8
from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import BaseComment


class BaseCommentForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = BaseComment
        fields = ('content', 'content_type', 'object_id')
