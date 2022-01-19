"""news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app_news.views import *
from app_users.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Redirect.as_view()),
    path('news_list/', NewsListView.as_view(), name='news_list'),
    path('news_list/<int:news_id>', NewsDetailView.as_view(), name='news_detail'),
    path('news_create/', NewsFormView.as_view()),
    path('news_edit/<int:news_id>/', NewsFormEditView.as_view()),
    path('comment_create/<int:news_id>', CommentaryFormView.as_view()),
    path('__debug__/', include('debug_toolbar.urls')),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('account/', AccountView.as_view(), name='account'),
    path('files/', include('app_media.urls')),

]
