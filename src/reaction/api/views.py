from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .serializers import ReactionSerializer
from ..models import Reaction


class ReactionsView(APIView):
    def get(self, request, *args, **kwargs):
        reaction = Reaction.objects.all()
        serializer = ReactionSerializer(reaction, many=True)
        return Response(data=serializer.data)

    @swagger_auto_schema(request_body=ReactionSerializer)
    def post(self, request, *args, **kwargs):
        serializer = ReactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReactionView(APIView):
    def get(self, request, reaction_id, *args, **kwargs):
        reaction = get_object_or_404(Reaction, pk=reaction_id)
        serializer = ReactionSerializer(reaction)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ReactionSerializer)
    def put(self, request, reaction_id, *args, **kwargs):
        reaction = get_object_or_404(Reaction, pk=reaction_id)
        serializer = ReactionSerializer(reaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, reaction_id, *args, **kwargs):
        reaction = get_object_or_404(Reaction, pk=reaction_id)
        reaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
