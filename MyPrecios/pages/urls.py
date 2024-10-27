from django.urls import path
from . import views
urlpatterns = [
   path('', views.home_page, name='home'),
   path('send', views.SendMessage.as_view(),name='send'),

]