
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sessions.models import Session
from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, ListView, FormView, DetailView
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from pages.models import Mails
from .forms import SendMessageForm, CreateDraftForm
from rest_framework import generics, viewsets, mixins
from .serializers import MailsSerializer

class MailsViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = MailsSerializer


    def get_queryset(self):
        return Mails.objects.all()[:3]

    @action(methods=['get'],detail=False)
    def session(self, request, *args, **kwargs):
        data = Session.objects.all()
        d = [{"key":session.session_key,
              "data":session.expire_date} for session in data]
        return Response({'data': d})












# class MainPageApiView(ListCreateAPIView):
#     queryset = Mails.objects.all()
#     serializer_class = MailsSerializer
#
# class MainPageUpdateApiView(UpdateAPIView):
#     queryset = Mails.objects.all()
#     serializer_class = MailsSerializer
#
# class MainPageDetailApiView(RetrieveUpdateDestroyAPIView):
#     serializer_class = MailsSerializer
#     queryset = Mails.objects.all()


# class MainPageApiView(APIView):
#     def get(self, request):
#         lst = Mails.objects.all()
#         return Response({'posts': MainPageSerializer(lst, many=True).data})
#
#     def post(self, request):
#         serializer = MainPageSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request , *args, **kwargs):
#         pk = kwargs.get('pk',None)
#         if not pk:
#             return Response({'error': 'Pk must be provided'})
#         try:
#             instance = Mails.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Mail does not exist'})
#         serializer = MainPageSerializer(data=request.data,instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Pk must be provided'})
#         try:
#             instance = Mails.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Mail does not exist'})
#
#         serializer = MainPageSerializer(instance=instance)
#         serializer.delete(instance)
#         return Response({'post': f"deleted post { pk }"})



