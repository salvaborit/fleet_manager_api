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

from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.response import Response


# @api_view(['GET'])
# def VehicleViewSet(request, format=None):
#     """ route 'tasks/' """

#     if request.method == 'GET':
#         tasks = Vehicle.objects.all()
#         serializer = VehicleSerializer(tasks, many=True)
#         return Response({"tasks": serializer.data}, headers={'Access-Control-Allow-Headers': 'access-control-allow-origin'})

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
