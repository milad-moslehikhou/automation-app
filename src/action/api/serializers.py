from rest_framework import serializers
from ..models.action import Action


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ['id', 'subject', 'match_case', 'description']
