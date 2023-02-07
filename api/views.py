from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters

from .models import Vehicle
from .models import Driver
from .models import VehicleDocumentation
from .models import DriverDocumentation

from .serializers import VehicleSerializer
from .serializers import DriverSerializer
from .serializers import VehicleDocumentationSerializer
from .serializers import DriverDocumentationSerializer

from .filters import VehicleFilter
from .filters import VehicleDocumentationFilter
from .filters import DriverFilter
from .filters import DriverDocumentationFilter


class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = VehicleFilter


class DriverViewSet(ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = DriverFilter


class VehicleDocumentationViewSet(ModelViewSet):
    queryset = VehicleDocumentation.objects.all()
    serializer_class = VehicleDocumentationSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = VehicleDocumentationFilter


class DriverDocumentationViewSet(ModelViewSet):
    queryset = DriverDocumentation.objects.all()
    serializer_class = DriverDocumentationSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = DriverDocumentationFilter
