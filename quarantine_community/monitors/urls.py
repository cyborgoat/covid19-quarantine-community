from django.contrib.auth.decorators import login_required
from django.urls import path, include
from rest_framework import routers

from monitors import views

app_name = "monitors"

urlpatterns = [
    path('', views.DrinkingWaterView.as_view(), name='monitor-drinking-watre'),

]
