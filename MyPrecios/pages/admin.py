from django.contrib import admin

# Register your models here.
from django.contrib import admin
# Импорт модели MyModel из текущего каталога (".")
from .models import Mails
# Регистрация модели MyModel для административного сайта
admin.site.register(Mails)