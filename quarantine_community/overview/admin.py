from django.contrib import admin

# Register your models here.
from overview.models import  User,CovidBasicInfo

admin.site.register(User)
admin.site.register(CovidBasicInfo)