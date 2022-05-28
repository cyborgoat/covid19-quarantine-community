from django.contrib.auth.decorators import login_required
from django.urls import  path

from overview import  views

app_name = "overview"

urlpatterns = [
    path('',views.OverviewView.as_view(),name='overview'),
]