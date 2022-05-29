from django.contrib.auth.decorators import login_required
from django.urls import path, include
from rest_framework import routers

from plaza import views

app_name = "plaza"


urlpatterns = [
    path('notifications/', views.OfficialNotificationsView.as_view(), name='official-notifications'),
    path('special-request-form/', views.AddSpecialRequestView.as_view(), name='special-request-form'),
    path('supply-registration-form/', views.AddSupplyRegistrationView.as_view(), name='supply-registration-form'),
]
