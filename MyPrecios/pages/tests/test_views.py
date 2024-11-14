from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from pages.models import *
import json

class TestViews(TestCase):
    def setUp(self):
        client = Client()
        self.url_main = reverse('home')
        self.url_detail = reverse('messsage', args=[27])
        User.objects.create_user(username='root', password='1234')
        User.objects.create_user(username='new', password='12')
        Mails.objects.create(pk=27,from_user='root', to_user='new',message='fdsafa')


    def test_main_page_view_no_auth(self):
        response = self.client.get(self.url_main)
        self.assertEqual(response.status_code, 302)

    def test_main_page_view_auth(self):
        self.client.login(username="root", password="1234")
        response = self.client.get(self.url_main)
        self.assertEqual(response.status_code, 200)

    def test_detail_view_auth(self):
        self.client.login(username="root", password="1234")
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data["object"].from_user, 'root')
        self.assertEqual(response.context_data["object"].to_user, 'new')
        self.assertEqual(response.context_data["object"].message, 'fdsafa')

    def test_send_message_view_auth(self):
        url_send = reverse('send')
        self.client.login(username="root", password="1234")
        response = self.client.post(url_send, {'message': 'testig', 'from_user': 'root', 'to_user': 'new'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Mails.objects.filter(message='testig').count(), 1)

    def test_send_message_view_auth_no_user(self):
        url_send = reverse('send')
        self.client.login(username="root", password="1234")
        response = self.client.post(url_send, {'message': 'testig', 'from_user': 'root', 'to_user': 'no_user'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Mails.objects.filter(message='testig').count(), 0)

