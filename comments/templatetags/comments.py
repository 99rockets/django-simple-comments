# coding: utf-8
from django import template, forms
from django.contrib.contenttypes.models import ContentType

from ..forms import BaseCommentForm
from ..models import BaseComment

register = template.Library()


@register.inclusion_tag('comment_form.html', takes_context=True)
def comment_form(context, obj):
    form = BaseCommentForm()
    object_type = ContentType.objects.get_for_model(obj)
    form.fields['content_type'].initial = object_type.id
    form.fields['object_id'].initial = obj.pk
    form.fields['content_type'].widget = forms.HiddenInput()
    form.fields['object_id'].widget = forms.HiddenInput()
    return {'form': form}


@register.inclusion_tag('comment_list.html')
def comment_list(obj):
    object_type = ContentType.objects.get_for_model(obj)
    comments = BaseComment.objects.filter(
        content_type__pk=object_type.id, object_id=obj.id
    )
    return {'comments': comments}
