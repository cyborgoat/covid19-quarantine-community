from django.db import models

# Create your models here.
from overview.models import User


class CountryYard(models.Model):
    yard_num = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.yard_num}号院'


class BuildingUnit(models.Model):
    unit_num = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.unit_num}号楼'


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
    responder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='responder')
    body = models.TextField()

    def __str__(self):
        return self.title


class SupplyItem(models.Model):
    name = models.CharField(max_length=32)
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class SupplyRegistration(models.Model):
    country_yard = models.ForeignKey(CountryYard,on_delete=models.CASCADE,related_name='country_yard')
    building_unit = models.ForeignKey(BuildingUnit,on_delete=models.CASCADE,related_name='building_unit')
    room_num = models.CharField(max_length=16)
    items = models.ManyToManyField(SupplyItem)


