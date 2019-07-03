
from django import forms
from .models import Hashtag, Blogpost


class TagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['tag']
        labels = {'tag': 'хэштэг'}


class PostForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ['tag', 'title', 'text']
        labels = {'title': '', 'text': '', 'tag': 'хэштэг'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80}),
                   'title': forms.Textarea(attrs={'cols': 80, 'rows': 1})}
