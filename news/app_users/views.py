from django.shortcuts import render
from app_users.forms import AuthForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth.views import LoginView
import datetime



# class LoginView(View):
#
#     def get(self, request):
#         auth_form = AuthForm()
#         return render(request, 'login.html', {'form':auth_form})
#
#     def post(self, request):
#         auth_form = AuthForm(request.POST)
#         if auth_form.is_valid():
#             username = auth_form.cleaned_data['username']
#             password = auth_form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponseRedirect('/news_list/')
#                 else:
#                     auth_form.add_error('__all__', 'Учетная запись пользователя не активна')
#                     return render(request, 'login.html', {'form': auth_form})
#             else:
#                 auth_form.add_error('__all__', 'Неправильный логин или пароль')
#                 return render(request, 'login.html', {'form': auth_form})
#         else:
#             return render(request, 'login.html', {'form':auth_form})


def login_view(request):
    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        now = datetime.datetime.now()
        if auth_form.is_valid():

            now = datetime.datetime.now()
            if now.hour <= 8 or now.hour > 22:
                auth_form.add_error(None, 'Авторизация недоступна c 8 до 22 часов')

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


class QuickLoginView(LoginView):
    template_name = 'login.html'
