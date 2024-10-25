from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView , TemplateView, ListView

class HomePageView(ListView):
    pass


def home_page(request):
    return render(request, 'pages/home_page.html',context={})

def main_page(request):
    return render(request, 'pages/main_page.html',context={})

def register_page(request):
    return render(request, 'pages/register_page.html',context={})