from rest_framework.viewsets import ModelViewSet

from .models import Vehicle
from .models import Driver
from .models import VehicleDocumentation
from .models import DriverDocumentation

from .serializers import VehicleSerializer
from .serializers import DriverSerializer
from .serializers import VehicleDocumentationSerializer
from .serializers import DriverDocumentationSerializer


class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class DriverViewSet(ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class VehicleDocumentationViewSet(ModelViewSet):
    queryset = VehicleDocumentation.objects.all()
    serializer_class = VehicleDocumentationSerializer


class DriverDocumentationViewSet(ModelViewSet):
    queryset = DriverDocumentation.objects.all()
    serializer_class = DriverDocumentationSerializer
