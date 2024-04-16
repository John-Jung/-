from django.forms import ModelForm
from .models import *

class NoticeBoardPostForm(ModelForm):
    class Meta:
        model = NoticeBoardPost
        fields = ['title', 'content', 'imgfile']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']