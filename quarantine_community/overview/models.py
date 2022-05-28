from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import datetime


# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to="uploads/images/avatars", blank=True, null=True)
    full_name = models.CharField(max_length=64, unique=False, blank=True, null=True)

    class Meta:
        app_label = 'overview'


class CovidBasicInfo(models.Model):
    quarantine_start_date = models.DateTimeField()
