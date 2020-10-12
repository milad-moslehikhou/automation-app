from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .serializers import ExecutionSerializer
from ..models import Execution


class ExecutionsView(APIView):
    def get(self, request, *args, **kwargs):
        executions = Execution.objects.all()
        serializer = ExecutionSerializer(executions, many=True)
        return Response(data=serializer.data)

    @swagger_auto_schema(request_body=ExecutionSerializer)
    def post(self, request, *args, **kwargs):
        serializer = ExecutionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExecutionView(APIView):
    def get(self, request, execution_id, *args, **kwargs):
        execution = get_object_or_404(Execution, pk=execution_id)
        serializer = ExecutionSerializer(execution)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ExecutionSerializer)
    def put(self, request, execution_id, *args, **kwargs):
        execution = get_object_or_404(Execution, pk=execution_id)
        serializer = ExecutionSerializer(execution, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, execution_id, *args, **kwargs):
        execution = get_object_or_404(Execution, pk=execution_id)
        execution.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
