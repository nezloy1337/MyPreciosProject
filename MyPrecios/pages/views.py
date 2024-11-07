
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, ListView, FormView, DetailView
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView

from pages.models import Mails
from .forms import SendMessageForm, CreateDraftForm

from rest_framework import generics

from .serializers import MainPageSerializer


class MainPageApiView(APIView):
    def get(self, request):
        lst = Mails.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request, *args, **kwargs):
        post_new = Mails.objects.create(
            from_user = request.data['from_user'],
            to_user = request.data['to_user'],
            message = request.data['message'],
        )
        return Response({'post': model_to_dict(post_new)})


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

class SendMessage(LoginRequiredMixin,FormView):
    form_class = SendMessageForm
    template_name = 'pages/sendform.html'
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.from_user = self.request.user.username
        form.save()
        return super().form_valid(form)

class ShowDraft(MainPage):
    template_name = 'pages/drafts.html'
    def get_queryset(self):
        return Mails.objects.filter(Q(from_user=self.request.user.username) & Q(is_draft=True))

class CreateDraft(LoginRequiredMixin,FormView):
    form_class = CreateDraftForm
    template_name = 'pages/drafts_form.html'
    success_url = reverse_lazy("drafts")

    def form_valid(self, form):
        form.instance.from_user = self.request.user.username
        form.instance.is_draft= True
        form.save()
        return super().form_valid(form)

class EditDraft(LoginRequiredMixin,UpdateView):
    model = Mails
    template_name = 'pages/drafts_form.html'
    fields = ['to_user', 'message' , 'is_draft']
    success_url = reverse_lazy("drafts")





class ShowMessage(LoginRequiredMixin,DetailView):
    model = Mails
    template_name = 'pages/show_message.html'
    slug_url_kwarg = 'message_id'
    context_object_name = 'message'

    def get_object(self):
        return get_object_or_404(Mails,id=self.kwargs['message_id'])


