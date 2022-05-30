from django.contrib.auth.models import Group
from rest_framework import serializers

from plaza.models import SupplyRegistration, SpecialRequest


class SupplyRegistrationSerializer(serializers.ModelSerializer):
    items = serializers.StringRelatedField(many=True, read_only=True)
    country_yard = serializers.StringRelatedField(many=False, read_only=True)
    building_unit = serializers.StringRelatedField(many=False, read_only=True)
    building_subunit = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = SupplyRegistration
        fields = '__all__'


class SpecialRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialRequest
        fields = '__all__'
