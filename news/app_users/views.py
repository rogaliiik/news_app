from django.shortcuts import render, redirect
from app_users.forms import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
import datetime
from app_users.models import *


def login_view(request):
    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        now = datetime.datetime.now()
        if auth_form.is_valid():

            now = datetime.datetime.now()
            # if now.hour <= 8 or now.hour > 22:
            #     auth_form.add_error(None, 'Авторизация недоступна c 8 до 22 часов')

            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_superuser:
                    auth_form.add_error('__all__', 'Авторизация недоступна')
                else:
                    if user.is_active:
                        if auth_form.has_error('__all__') == False:
                            login(request, user)
                            return HttpResponseRedirect('/news_list/')
                    else:
                        auth_form.add_error('__all__', 'Учетная запись пользователя не активна')
            else:
                auth_form.add_error('__all__', 'Неправильный логин или пароль')
    else:
        auth_form = AuthForm()
    return render(request, 'login.html', {'form':auth_form})


class LogoutView(LogoutView):
    next_page = '/'


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            city = form.cleaned_data.get('city')
            date_of_birth = form.cleaned_data.get('date_of_birth')
            phone_number = form.cleaned_data.get('phone_number')
            card_number = form.cleaned_data.get('card_number')
            Profile.objects.create(
                user=user,
                city=city,
                date_of_birth=date_of_birth,
                phone_number=phone_number,
                card_number=card_number,
            )
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm(request.POST)
    return render(request, 'register.html', {'form':form})


class AccountView(View):

    def get(self, request):
        user = request.user
        return render(request, 'account.html', {'user':user})