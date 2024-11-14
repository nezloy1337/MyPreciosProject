

from django.test import TestCase
from django.urls import reverse, resolve
from pages.views import *


class TestUrls(TestCase):

    def test_main_page(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, MainPage)