from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions

from overview.models import User, CovidBasicInfo
from overview.serializers import UserSerializer, GroupSerializer, CovidBasicInfoSerializer


class OverviewView(TemplateView):
    template_name = "overview/index.html"

    def get_context_data(self, **kwargs):
        context = super(OverviewView, self).get_context_data(**kwargs)
        return context


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-first_name')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]


class CovidBasicInfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = CovidBasicInfo.objects.all().order_by('-quarantine_start_date')
    serializer_class = CovidBasicInfoSerializer
    # permission_classes = [permissions.IsAuthenticated]
