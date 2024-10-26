from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView , TemplateView, ListView

class HomePageView(ListView):
    pass


@login_required
def home_page(request):
    return render(request, 'pages/main_page.html',context={})
