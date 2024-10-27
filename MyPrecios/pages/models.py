from django.db import models


class Mails(models.Model):
    from_user =models.CharField(max_length=50,blank=True)
    to_user = models.CharField(max_length=50,blank=True)
    message = models.TextField(blank=True,)
    sent_at = models.DateTimeField(auto_now=True)
