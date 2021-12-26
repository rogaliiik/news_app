from app_news.models import *
from django import forms


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = '__all__'


class CommentaryForm(forms.ModelForm):

    class Meta:
        model = Commentary
        fields = '__all__'