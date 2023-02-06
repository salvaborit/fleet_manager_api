from rest_framework.views import APIView
from rest_framework.response import Response


class APIStatus(APIView):
    """ route 'status/' """

    def get(self, request):
        return Response({'status': 'true'})
