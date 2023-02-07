from django_filters import rest_framework as filters


class VehicleFilter(filters.FilterSet):
    license_plate = filters.CharFilter(
        field_name='license_plate',
        lookup_expr='contains')
