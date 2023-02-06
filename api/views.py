from rest_framework.viewsets import ModelViewSet

from .models import Vehicle
from .models import VehicleModel
from .models import Documentation

from .serializers import VehicleSerializer
from .serializers import VehicleModelSerializer
from .serializers import DocumentationSerializer


class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleModelViewSet(ModelViewSet):
    queryset = VehicleModel.objects.all()
    serializer_class = VehicleModelSerializer


class DocumentationViewSet(ModelViewSet):
    queryset = Documentation.objects.all()
    serializer_class = DocumentationSerializer
