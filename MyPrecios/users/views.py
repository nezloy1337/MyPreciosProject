from django.contrib.auth import get_user_model, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.defaultfilters import title
from django.urls import reverse_lazy, reverse

from users.forms import LoginUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {title:'avrtoriz'}

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))
