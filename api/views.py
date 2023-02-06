from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TestModel
from .serializers import TestSerializer

class APIStatus(APIView):
    def get(self, request):
        return Response({'status': 'true'})


# "This is a viewset that will
# handle all of the operations for the TestModel model, and will use the
# TestSerializer serializer to serialize and deserialize the data."
#
# The `ModelViewSet` class inherits from the `GenericViewSet` class, which inherits
# from the `ViewSet` class, which inherits from the `APIView` class
class TestViewSet(ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer