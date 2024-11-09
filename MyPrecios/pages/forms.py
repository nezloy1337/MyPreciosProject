from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from pages.models import Mails

# @deconstructible
# class UserValidator:
#     allowed_names = User.objects.all().values_list('username', flat=True)
#     code = 'users'
#
#     def __init__(self, name = None):
#         self.name = name if name else 'enter something'
#
#     def __call__(self, name):
#         if not self.name in self.allowed_names:
#             raise ValidationError(self.name, code=self.code)


class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Mails
        fields = [ 'to_user', 'message' ]
        widgets = {
            'to_user': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }

    def clean_to_user(self):
        to_user = self.cleaned_data['to_user']
        users = User.objects.all().values_list('username', flat=True)
        if to_user not in users:
            raise ValidationError('there is no user with this username')
        return to_user

class CreateDraftForm(SendMessageForm):
    pass