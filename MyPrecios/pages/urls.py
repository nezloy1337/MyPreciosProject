from django.urls import path
from . import views
urlpatterns = [
   path('', views.MainPage.as_view(), name='home'),
   path('send', views.SendMessage.as_view(),name='send'),
   path('outcome', views.OutcomeMessages.as_view(),name='outcome'),
   path('message/<int:message_id>', views.ShowMessage.as_view(),name='messsage'),
   path('draft', views.ShowDraft.as_view(),name='drafts'),


]