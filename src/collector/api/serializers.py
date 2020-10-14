from rest_framework import serializers


class CollectorSerializer(serializers.Serializer):
    data = serializers.CharField(max_length=255)
