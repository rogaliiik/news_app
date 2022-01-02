from django.shortcuts import render, redirect
from django.views.generic import View, DetailView, ListView
from app_news.models import *
from app_news.forms import *
from django.http import HttpResponseRedirect, HttpResponse

class Redirect(View):
    def get(self, request):
        return redirect('/news_list')


class NewsListView(ListView):
    template_name = 'news_list.html'
    context_object_name = 'news'
    queryset = News.objects.all()


class NewsDetailView(View):
    def get(self, request, news_id):
        news = News.objects.get(id=news_id)
        comments = Commentary.objects.filter(news=news)
        return render(request, 'news_detail.html', {'news':news, 'comments':comments})


class NewsFormView(View):
    def get(self, request):
        news_form = NewsForm()
        return render(request, 'news_create.html', {'news_form':news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)

        if news_form.is_valid():
            News.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect('/news_list')
        else:
            return render(request, 'news_create.html', {'news_form':news_form})


class NewsFormEditView(View):
    def get(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = NewsForm(instance=news)
        return render(request, 'news_edit.html', {'news_form':news_form, 'news_id':news_id})

    def post(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = NewsForm(request.POST, instance=news)

        if news_form.is_valid():
            news.save()
            return render(request, 'news_edit.html', context={'news_form': news_form, 'news_id':news_id})


class CommentaryFormView(View):
    def get(self, request, news_id):
        news = News.objects.get(id=news_id)
        if request.user.is_authenticated:
            comment_form = CommentaryFormAuth()
        else:
            comment_form = CommentaryFormNotAuth()
        return render(request, 'comment_create.html', {'comment_form':comment_form, 'news':news})

    def post(self, request, news_id):
        news = News.objects.get(id=news_id)
        if request.user.is_authenticated:
            comment_form = CommentaryFormAuth(request.POST)
            if comment_form.is_valid():
                Commentary.objects.create(**comment_form.cleaned_data, user_name=request.user.username, user=request.user,
                                          news=news)
                return HttpResponseRedirect('/news_list/' + str(news_id))
            else:
                return render(request, 'comment_create.html', {'comment_form': comment_form, 'news':news})
        else:
            comment_form = CommentaryFormNotAuth(request.POST)
            if comment_form.is_valid():
                user_name = comment_form.cleaned_data['user_name']
                description = comment_form.cleaned_data['description']
                Commentary.objects.create(user_name = user_name + ' Гость', description=description, news=news)
                return HttpResponseRedirect('/news_list/' + str(news_id))
            else:
                return render(request, 'comment_create.html', {'comment_form':comment_form, 'news':news})
