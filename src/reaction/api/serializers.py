from rest_framework import serializers
from ..models.reaction import Reaction


class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ['id', 'subject', 'script', 'description']
