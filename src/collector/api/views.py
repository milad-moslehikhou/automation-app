from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .serializers import CollectorSerializer
from ..tasks import process_data


class CollectorView(APIView):
    @swagger_auto_schema(request_body=CollectorSerializer)
    def post(self, request, *args, **kwargs):
        serializer = CollectorSerializer(data=request.data)
        if serializer.is_valid():
            process_data.delay(serializer.data)
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
