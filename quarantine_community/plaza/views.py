from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView
from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.
from plaza.models import OfficialNotification
from django.utils import timezone


class OfficialNotificationsView(ListView):
    model = OfficialNotification
    paginate_by = 100  # if pagination is desired
    context_object_name = 'notification_list'
    queryset = OfficialNotification.objects.filter(active=True)
    template_name = "plaza/official-notifications/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
