from django.urls import path
from django.views.decorators.cache import cache_page

from . import views
urlpatterns = [
   path('', views.MainPage.as_view(), name='home'),
   path('send', views.SendMessage.as_view(),name='send'),
   path('outcome', views.OutcomeMessages.as_view(),name='outcome'),
   path('message/<int:message_id>', views.ShowMessage.as_view(),name='messsage'),
   path('draft', views.ShowDraft.as_view(),name='drafts'),
   path('draft_cache',cache_page(60)(views.ShowDraft.as_view()),name='drafts_cache'),
   path('createdraft', views.CreateDraft.as_view(),name='createdraft'),
   path('editdraft/<int:pk>', views.EditDraft.as_view(),name='editdraft'),


]