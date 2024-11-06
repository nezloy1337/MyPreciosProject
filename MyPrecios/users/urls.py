from django.contrib.auth.views import LogoutView
from django.views.decorators.cache import cache_page
from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [
   path('login/', cache_page(60)(views.LoginUser.as_view()), name='login'),
   path('logout/', views.logout_user, name='logout'),
   path('register/', views.RegisterUser.as_view(), name='register'),

]