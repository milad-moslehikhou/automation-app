from rest_framework import serializers
from ..models.task import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'action', 'reaction', 'subject', 'enable']
