from django_filters import rest_framework as filters

from .models import Vehicle
from .models import Driver
from .models import VehicleDocumentation
from .models import DriverDocumentation


class VehicleFilter(filters.FilterSet):
    license_plate = filters.CharFilter(
        field_name='license_plate',
        lookup_expr='contains')
    model = filters.CharFilter(
        field_name='model',
        lookup_expr='contains')
    status = filters.CharFilter(
        field_name='status',
        lookup_expr='contains')
    usage_type = filters.CharFilter(
        field_name='usage_type',
        lookup_expr='contains')
    min_usage = filters.NumberFilter(
        field_name='usage',
        lookup_expr='gte')
    max_usage = filters.NumberFilter(
        field_name='usage',
        lookup_expr='lte')
    notes = filters.NumberFilter(
        field_name='notes',
        lookup_expr='contains')

    class Meta:
        model = Vehicle
        fields = ['license_plate', 'model', 'status',
                  'usage_type', 'usage', 'notes']


class DriverFilter(filters.FilterSet):
    first_name = filters.CharFilter(
        field_name='first_name',
        lookup_expr='contains')
    last_name = filters.CharFilter(
        field_name='last_name',
        lookup_expr='contains')
    address = filters.CharFilter(
        field_name='address',
        lookup_expr='contains')
    email = filters.CharFilter(
        field_name='email',
        lookup_expr='contains')
    phone = filters.CharFilter(
        field_name='phone',
        lookup_expr='contains')
    birthdate = filters.DateFilter(
        field_name='birthdate')
    id_type = filters.CharFilter(
        field_name='id_type',
        lookup_expr='contains')
    id_number = filters.CharFilter(
        field_name='id_number',
        lookup_expr='contains')

    class Meta:
        model = Driver
        fields = ['first_name', 'last_name', 'address',
                  'email', 'phone', 'birthdate', 'id_type', 'id_number']


class VehicleDocumentationFilter(filters.FilterSet):
    title = filters.CharFilter(
        field_name='title',
        lookup_expr='contains')
    vehicle = filters.NumberFilter(
        field_name='vehicle')
    valid_thru = filters.DateFilter(
        field_name='valid_thru')
    renovation_alert = filters.DateTimeFilter(
        field_name='renovation_alert')
    status = filters.CharFilter(
        field_name='status',
        lookup_expr='contains')

    class Meta:
        model = VehicleDocumentation
        fields = ['title', 'vehicle', 'valid_thru',
                  'renovation_alert', 'status']


class DriverDocumentationFilter(filters.FilterSet):
    title = filters.CharFilter(
        field_name='title',
        lookup_expr='contains')
    driver = filters.NumberFilter(
        field_name='driver')
    valid_thru = filters.DateFilter(
        field_name='valid_thru')
    renovation_alert = filters.DateTimeFilter(
        field_name='renovation_alert')
    status = filters.CharFilter(
        field_name='status',
        lookup_expr='contains')

    class Meta:
        model = DriverDocumentation
        fields = ['title', 'driver', 'valid_thru',
                  'renovation_alert', 'status']
