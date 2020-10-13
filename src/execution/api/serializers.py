from rest_framework import serializers
from ..models.execution import Execution


class ExecutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Execution
        fields = ['id', 'task', 'start_at', 'end_at', 'stdout', 'stderr', 'status']
