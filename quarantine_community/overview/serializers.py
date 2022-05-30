from django.contrib.auth.models import Group
from rest_framework import serializers

from overview.models import CovidBasicInfo, User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class CovidBasicInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CovidBasicInfo
        fields = ['name', 'quarantine_start_date', 'expected_end_date']
