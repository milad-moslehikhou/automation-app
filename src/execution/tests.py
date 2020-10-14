from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import datetime

from action.models import Action
from reaction.models import Reaction
from task.models import Task
from .models import Execution


class ExecutionTest(APITestCase):
    sampleAction = Action(
        id='1',
        subject='subject-test',
        match_case='match-case-test',
        description='description-test'
    )
    sampleReaction = Reaction(
        id='1',
        subject='subject-test',
        script='print("test")',
        description='description-test'
    )
    sampleTask = Task(
        id=1,
        action=sampleAction,
        reaction=sampleReaction,
        subject='subject-test',
        enable=True,
    )
    sampleExecution = Execution(
        task=sampleTask,
        start_at=datetime.now(),
        end_at=datetime.now(),
        status="OK",
        stderr="",
        stdout="",
    )

    def test_get_execution(self):
        self.sampleAction.save()
        self.sampleReaction.save()
        self.sampleTask.save()
        self.sampleExecution.save()
        url = reverse('executions:executions')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
