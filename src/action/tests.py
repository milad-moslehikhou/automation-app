from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from . import models


class ActionTest(APITestCase):

    sampleAction = models.Action(
        subject='subject-test',
        match_case='match-case-test',
        description='description-test'
    )

    def test_create_action(self):
        url = reverse('actions:actions')
        data = {
            'subject': 'subject-test',
            'match_case': 'match-case-test',
            'description': 'description-test'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Action.objects.get().subject, 'subject-test')

    def test_get_action(self):
        self.sampleAction.save()
        url = reverse('actions:actions')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_action(self):
        self.sampleAction.save()
        url = reverse('actions:action', kwargs={'action_id': 1})
        data = {
            'subject': 'subject-edit-test',
            'match_case': 'match-case-edit-test',
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Action.objects.get().subject, 'subject-edit-test')

    def test_delete_action(self):
        self.sampleAction.save()
        url = reverse('actions:action', kwargs={'action_id': 1})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(models.Action.objects.all()), 0)
