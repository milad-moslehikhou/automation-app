from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .serializers import ActionSerializer
from ..models import Action


class ActionsView(APIView):
    def get(self, request, *args, **kwargs):
        actions = Action.objects.all()
        serializer = ActionSerializer(actions, many=True)
        return Response(data=serializer.data)

    @swagger_auto_schema(request_body=ActionSerializer)
    def post(self, request, *args, **kwargs):
        serializer = ActionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActionView(APIView):
    def get(self, request, action_id, *args, **kwargs):
        action = get_object_or_404(Action, pk=action_id)
        serializer = ActionSerializer(action)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ActionSerializer)
    def put(self, request, action_id, *args, **kwargs):
        action = get_object_or_404(Action, pk=action_id)
        serializer = ActionSerializer(action, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, action_id, *args, **kwargs):
        action = get_object_or_404(Action, pk=action_id)
        action.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
