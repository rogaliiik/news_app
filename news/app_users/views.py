from django.shortcuts import render
from app_users.forms import AuthForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.views import View


class LoginView(View):

    def get(self, request):
        auth_form = AuthForm()
        return render(request, 'login.html', {'form':auth_form})

    def post(self, request):
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/news_list/')
                else:
                    auth_form.add_error('__all__', 'Учетная запись пользователя не активна')
                    return render(request, 'login.html', {'form': auth_form})
            else:
                auth_form.add_error('__all__', 'Неправильный логин или пароль')
                return render(request, 'login.html', {'form': auth_form})
        else:
            return render(request, 'login.html', {'form':auth_form})