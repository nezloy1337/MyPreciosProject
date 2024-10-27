from django import forms
from django.contrib.auth.forms import AuthenticationForm

from pages.models import Mails


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин",
                    widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль",
                    widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Mails
        fields = [ 'to_user', 'message']
        widgets = {
            'to_user': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }
