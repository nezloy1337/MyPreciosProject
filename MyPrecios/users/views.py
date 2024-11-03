from mailbox import Message

from django.contrib.auth import get_user_model, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.defaultfilters import title
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from users.forms import LoginUserForm,  CreateUserForm


class LoginUser(LoginView):
    model = User
    form_class = LoginUserForm
    template_name = 'users/login.html'

class RegisterUser(CreateView):
    form_class = UserCreationForm
    model = User
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))


