from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from pages.forms import SendMessageForm
from pages.models import *
import json

class TestForms(TestCase):
    def setUp(self):
        client = Client()
        User.objects.create_user(username='root', password='1234')
        User.objects.create_user(username='new', password='12')


    def test_form_true(self):
        form = SendMessageForm(data={
            "from_user":"root",
            "to_user":"new",
            "message":"testform",
        })
        self.assertTrue(form.is_valid())

    def test_form_false(self):
        form = SendMessageForm(data={
            "from_user": "root",
            "to_user": "nouser",
            "message": "testform",
        })
        self.assertFalse(form.is_valid())
