from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, ListView, FormView, DetailView
from django.db.models import Q
from pages.models import Mails
from users.forms import SendMessageForm



class MainPage(LoginRequiredMixin, ListView):
    model = Mails
    template_name = 'pages/main_page.html'
    context_object_name = 'mails'
    def get_queryset(self):
        return Mails.objects.filter(Q(to_user=self.request.user.username) & Q(is_draft=False))

class OutcomeMessages(MainPage):
    extra_context = {'bool':True}
    def get_queryset(self):
        return  Mails.objects.filter(Q(from_user=self.request.user.username) & Q(is_draft=False))

class ShowMessage(LoginRequiredMixin,DetailView):
    model = Mails
    template_name = 'pages/show_message.html'
    slug_url_kwarg = 'message_id'
    context_object_name = 'message'

    def get_object(self):
        return get_object_or_404(Mails,id=self.kwargs['message_id'])

class SendMessage(LoginRequiredMixin,FormView):
    form_class = SendMessageForm
    template_name = 'pages/sendform.html'
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.from_user = self.request.user.username
        form.save()
        return super().form_valid(form)


class ShowDraft(MainPage):
    def get_queryset(self):
        return Mails.objects.filter(Q(from_user=self.request.user.username) & Q(is_draft=True))



