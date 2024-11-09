from rest_framework import serializers

from pages.models import Mails



class MailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mails
        fields = ('from_user', 'to_user', 'message')





# class MainPageSerializer(serializers.Serializer):
#     from_user = serializers.CharField(max_length=255)
#     to_user = serializers.CharField(max_length=255)
#     message = serializers.CharField(max_length=255)
#
#     def create(self, validated_data):
#         return Mails.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.from_user = validated_data.get('from_user', instance.from_user)
#         instance.to_user = validated_data.get('to_user', instance.to_user)
#         instance.message = validated_data.get('message', instance.message)
#         instance.save()
#         return instance
#
#     def delete(self, instance):
#         instance.delete()
#         return instance