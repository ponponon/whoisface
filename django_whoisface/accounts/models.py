from django.db import models

# Create your models here.


class Status(models.IntegerChoices):
    UNDEFINE = (0, 'undefine')
    MAN = (1, 'man')
    WOMAN = (2, 'woman')


class Accounts(models.Model):
    username = models.CharField(max_length=128)
    age = models.IntegerField()
    gender = models.IntegerField(
        choices=Status.choices,
        default=Status.UNDEFINE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
