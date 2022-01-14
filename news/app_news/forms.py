from app_news.models import *
from django import forms


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title', 'description', 'tag']


class CommentaryFormNotAuth(forms.ModelForm):

    class Meta:
        model = Commentary
        fields = ['user_name', 'description']


class CommentaryFormAuth(forms.ModelForm):

    class Meta:
        model = Commentary
        fields = ['description']