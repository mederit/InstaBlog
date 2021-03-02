from django import forms
from . models import *
from django.forms import ModelForm, Textarea


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={'col': 80, 'rows': 2}),
        }
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'slug', 'photo', 'tags')














