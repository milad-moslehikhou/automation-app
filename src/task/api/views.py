from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .serializers import TaskSerializer
from ..models import Task


class TasksView(APIView):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(data=serializer.data)

    @swagger_auto_schema(request_body=TaskSerializer)
    def post(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskView(APIView):
    def get(self, request, task_id, *args, **kwargs):
        task = get_object_or_404(Task, pk=task_id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TaskSerializer)
    def put(self, request, task_id, *args, **kwargs):
        task = get_object_or_404(Task, pk=task_id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, task_id, *args, **kwargs):
        task = get_object_or_404(Task, pk=task_id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
