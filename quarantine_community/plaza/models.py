from django.db import models

# Create your models here.
from overview.models import User


class CountryYard(models.Model):
    yard_num = models.IntegerField()

    def __str__(self):
        return f'{self.yard_num}号院'


class BuildingUnit(models.Model):
    unit_num = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.unit_num}号楼'


class BuildingSubUnit(models.Model):
    unit_num = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.unit_num}单元'


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
    country_yard = models.ForeignKey(CountryYard, on_delete=models.CASCADE, related_name='cy_special')
    building_unit = models.ForeignKey(BuildingUnit, on_delete=models.CASCADE, related_name='bu_special')
    building_subunit = models.ForeignKey(BuildingSubUnit, on_delete=models.CASCADE, related_name='bs_special')
    room_num = models.CharField(max_length=16)
    body = models.TextField()

    resolved_by_staff = models.BooleanField(default=False)
    resolved_by_applicant = models.BooleanField(default=False)

    def __str__(self):
        return f'ticket{self.pk}-{self.country_yard}-{self.building_unit}-{self.room_num}'


class SupplyItem(models.Model):
    name = models.CharField(max_length=32)
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class SupplyRegistration(models.Model):
    country_yard = models.ForeignKey(CountryYard, on_delete=models.CASCADE, related_name='cy')
    building_unit = models.ForeignKey(BuildingUnit, on_delete=models.CASCADE, related_name='bu')
    building_subunit = models.ForeignKey(BuildingSubUnit, on_delete=models.CASCADE, related_name='bs')
    room_num = models.CharField(max_length=16)
    items = models.ManyToManyField(SupplyItem)
    resolved_by_staff = models.BooleanField(default=False)
    resolved_by_applicant = models.BooleanField(default=False)

    def __str__(self):
        return f'ticket{self.pk}-{self.country_yard}-{self.building_unit}-{self.room_num}'


class ItemConfirmation(models.Model):
    country_yard = models.ForeignKey(CountryYard, on_delete=models.CASCADE, related_name='cy_confirm')
    building_unit = models.ForeignKey(BuildingUnit, on_delete=models.CASCADE, related_name='bu_confirm')
    building_subunit = models.ForeignKey(BuildingSubUnit, on_delete=models.CASCADE, related_name='bs_confirm')
    supply_requests = models.ManyToManyField(SupplyRegistration)
    special_requests = models.ManyToManyField(SpecialRequest)

    # def __str__(