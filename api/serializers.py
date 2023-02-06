from rest_framework import serializers

from .models import Vehicle
from .models import VehicleModel
from .models import Documentation


class VehicleSerializer(serializers.ModelSerializer):
    model = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=VehicleModel.objects.all())
    Documentation = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Documentation.objects.all())

    class Meta:
        model = Vehicle
        fields = '__all__'


class VehicleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = '__all__'


class DocumentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documentation
        fields = '__all__'
