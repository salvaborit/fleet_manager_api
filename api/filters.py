from django_filters import rest_framework as filters

from .models import Vehicle
from .models import Driver
from .models import VehicleDocumentation
from .models import DriverDocumentation


class VehicleFilter(filters.FilterSet):
    license_plate = filters.CharFilter(
        field_name='license_plate',
        lookup_expr='icontains')
    model = filters.CharFilter(
        field_name='model',
        lookup_expr='icontains')
    status = filters.CharFilter(
        field_name='status',
        lookup_expr='icontains')
    usage_type = filters.CharFilter(
        field_name='usage_type',
        lookup_expr='icontains')
    min_usage = filters.NumberFilter(
        field_name='usage',
        lookup_expr='gte')
    max_usage = filters.NumberFilter(
        field_name='usage',
        lookup_expr='lte')
    notes = filters.CharFilter(
        field_name='notes',
        lookup_expr='icontains')

    class Meta:
        model = Vehicle
        fields = ['license_plate', 'model', 'status',
                  'usage_type', 'usage', 'notes']


class DriverFilter(filters.FilterSet):
    first_name = filters.CharFilter(
        field_name='first_name',
        lookup_expr='icontains')
    last_name = filters.CharFilter(
        field_name='last_name',
        lookup_expr='icontains')
    address = filters.CharFilter(
        field_name='address',
        lookup_expr='icontains')
    email = filters.CharFilter(
        field_name='email',
        lookup_expr='icontains')
    phone = filters.CharFilter(
        field_name='phone',
        lookup_expr='icontains')
    birthdate = filters.DateFilter(
        field_name='birthdate')
    id_type = filters.CharFilter(
        field_name='id_type',
        lookup_expr='icontains')
    id_number = filters.CharFilter(
        field_name='id_number',
        lookup_expr='icontains')

    class Meta:
        model = Driver
        fields = ['first_name', 'last_name', 'address',
                  'email', 'phone', 'birthdate', 'id_type', 'id_number']


class VehicleDocumentationFilter(filters.FilterSet):
    title = filters.CharFilter(
        field_name='title',
        lookup_expr='icontains')
    vehicle = filters.NumberFilter(
        field_name='vehicle')
    expiry = filters.DateFilter(
        field_name='expiry')
    renovation_alert = filters.NumberFilter(
        field_name='renovation_alert')

    class Meta:
        model = VehicleDocumentation
        fields = ['title', 'vehicle', 'expiry',
                  'renovation_alert']


class DriverDocumentationFilter(filters.FilterSet):
    title = filters.CharFilter(
        field_name='title',
        lookup_expr='icontains')
    driver = filters.NumberFilter(
        field_name='driver')
    expiry = filters.DateFilter(
        field_name='expiry')
    renovation_alert = filters.NumberFilter(
        field_name='renovation_alert')

    class Meta:
        model = DriverDocumentation
        fields = ['title', 'driver', 'expiry',
                  'renovation_alert']
