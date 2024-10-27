from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, ListView, FormView

from pages.models import Mails
from users.forms import SendMessageForm





# @login_required
# def home_page(request):
#     auth = request.user.is_authenticated
#     return render(request, 'pages/main_page.html',context={"auth":auth})


class MainPage(LoginRequiredMixin, ListView):
    model = Mails
    template_name = 'pages/main_page.html'
    context_object_name = 'mails'

    def get_queryset(self):
        return Mails.objects.filter(to_user=self.request.user.username)


class SendMessage(LoginRequiredMixin,FormView):
    form_class = SendMessageForm
    template_name = 'pages/sendform.html'
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.from_user = self.request.user.username
        form.save()

        return super().form_valid(form)

