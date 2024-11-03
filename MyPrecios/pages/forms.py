from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from pages.models import Mails


class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Mails
        fields = [ 'to_user', 'message']
        widgets = {
            'to_user': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }

class CreateDraftForm(SendMessageForm):
    pass