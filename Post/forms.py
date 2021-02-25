from django import forms
from .models import *


class CommentForm(forms.Form):
    class Meta:
        model = Comment
        fields = ('text',)
    body = forms.CharField(widget=forms.TextInput, label='Comment')