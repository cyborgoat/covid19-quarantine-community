from django.contrib import admin

# Register your models here.
from plaza.models import OfficialNotification, SpecialRequest, CountryYard, BuildingUnit, SupplyRegistration, \
    SupplyItem, BuildingSubUnit, DrinkingWaterRegistration, BentoBoxRequest


class WithTimeAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on',)


admin.site.register(OfficialNotification)
admin.site.register(SpecialRequest, WithTimeAdmin)
admin.site.register(CountryYard)
admin.site.register(BuildingUnit)
admin.site.register(BuildingSubUnit)
admin.site.register(SupplyRegistration, WithTimeAdmin)
admin.site.register(SupplyItem)
admin.site.register(DrinkingWaterRegistration, WithTimeAdmin)
admin.site.register(BentoBoxRequest, WithTimeAdmin)
