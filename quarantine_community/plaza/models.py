from django.db import models

# Create your models here.
from overview.models import User


class CountryYard(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class OfficialNotification(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    created_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class SpecialRequest(models.Model):
    title = models.CharField(max_length=64)
    name = models.CharField(max_length=32)
    responder = models.ForeignKey(User,on_delete=models.CASCADE,related_name='responder')
    body = models.TextField()

    def __str__(self):
        return self.title
