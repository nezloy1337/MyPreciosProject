from rest_framework import serializers

from pages.models import Mails



class MainPageSerializer(serializers.ModelSerializer):


    class Meta:
        model = Mails
        fields = ('from_user', 'message')