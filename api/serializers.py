from rest_framework import serializers

from .models import Vehicle
from .models import Driver
from .models import VehicleDocumentation
from .models import DriverDocumentation


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class VehicleDocumentationSerializer(serializers.ModelSerializer):
    vehicle = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Vehicle.objects.all())

    class Meta:
        model = VehicleDocumentation
        fields = '__all__'


class DriverDocumentationSerializer(serializers.ModelSerializer):
    driver = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Driver.objects.all())

    class Meta:
        model = DriverDocumentation
        fields = '__all__'
