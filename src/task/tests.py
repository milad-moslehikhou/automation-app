from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from action.models import Action
from reaction.models import Reaction
from task.models import Task


class TaskTest(APITestCase):
    sampleAction = Action(
        id=1,
        subject='subject-test',
        match_case='match-case-test',
        description='description-test'
    )
    sampleReaction = Reaction(
        id=1,
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

    def test_create_task(self):
        self.sampleAction.save()
        self.sampleReaction.save()
        url = reverse('tasks:tasks')
        data = {
            'action': 1,
            'reaction': 1,
            'subject': 'subject-test',
            'enable': True,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.get().subject, 'subject-test')

    def test_get_task(self):
        self.sampleAction.save()
        self.sampleReaction.save()
        self.sampleTask.save()
        url = reverse('tasks:tasks')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_task(self):
        self.sampleAction.save()
        self.sampleReaction.save()
        self.sampleTask.save()
        url = reverse('tasks:task', kwargs={'task_id': 1})
        data = {
            'action': 1,
            'reaction': 1,
            'subject': 'subject-edit-test',
            'enable': True,
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get().subject, 'subject-edit-test')

    def test_delete_task(self):
        self.sampleAction.save()
        self.sampleReaction.save()
        self.sampleTask.save()
        url = reverse('tasks:task', kwargs={'task_id': 1})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(Task.objects.all()), 0)
