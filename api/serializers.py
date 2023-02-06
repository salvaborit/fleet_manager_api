from rest_framework import serializers

from .models import Vehicle
from .models import Driver
from .models import VehicleModel
from .models import VehicleDocumentation
from .models import DriverDocumentation


class VehicleSerializer(serializers.ModelSerializer):
    model = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=VehicleModel.objects.all())

    class Meta:
        model = Vehicle
        fields = '__all__'


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class VehicleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = '__all__'


class VehicleDocumentationSerializer(serializers.ModelSerializer):
    vehicle = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Vehicle.objects.all())

    class Meta:
        model = VehicleDocumentation
        fields = '__all__'


class DriverDocumentationSerializer(serializers.ModelSerializer):
    driver = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Driver.objects.all())

    class Meta:
        model = DriverDocumentation
        fields = '__all__'
