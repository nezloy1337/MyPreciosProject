from django.urls import path
from . import views
urlpatterns = [
   path('', views.home_page, name='home_page'),
   path('main/', views.main_page, name='main_page'),
   path('register/', views.register_page, name='register_page'),
]