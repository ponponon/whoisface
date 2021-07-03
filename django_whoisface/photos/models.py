from django.db import models
from accounts.models import Accounts

# Create your models here.


class Photo(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.SET_NULL, null=True)
    filename = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
