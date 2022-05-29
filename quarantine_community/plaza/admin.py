from django.contrib import admin

# Register your models here.
from plaza.models import OfficialNotification, SpecialRequest,CountryYard,BuildingUnit,SupplyRegistration

admin.site.register(OfficialNotification)
admin.site.register(SpecialRequest)
admin.site.register(CountryYard)
admin.site.register(BuildingUnit)
admin.site.register(SupplyRegistration)