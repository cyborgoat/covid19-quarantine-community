from django.contrib import admin

# Register your models here.
from plaza.models import OfficialNotification, SpecialRequest

admin.site.register(OfficialNotification)
admin.site.register(SpecialRequest)