from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        
    # body = forms.CharField(widget=forms.TextInput, label='Comment')



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'slug')














