from django.shortcuts import render

def home_page(request):
    return render(request, 'pages/home_page.html',context={})

def main_page(request):
    return render(request, 'pages/main_page.html',context={})

def register_page(request):
    return render(request, 'pages/register_page.html',context={})