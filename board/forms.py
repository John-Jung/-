from django.forms import ModelForm, TextInput
from .models import *

class NoticeBoardPostForm(ModelForm):
    class Meta:
        model = NoticeBoardPost
        fields = ['title', 'content', 'imgfile']
        labels = {
            'title': '제목',
            'content': '내용',
            'imgfile': '이미지',
        }
       

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': TextInput(attrs={'placeholder': '댓글'}),
        }