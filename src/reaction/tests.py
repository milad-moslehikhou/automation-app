from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from . import models


class ReactionTest(APITestCase):

    sampleReaction = models.Reaction(
        subject='subject-test',
        script='print("test")',
        description='description-test'
    )

    def test_create_reaction(self):
        url = reverse('reactions:reactions')
        data = {
            'subject': 'subject-test',
            'script': 'print("test")',
            'description': 'description-test'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Reaction.objects.get().subject, 'subject-test')

    def test_get_reaction(self):
        self.sampleReaction.save()
        url = reverse('reactions:reactions')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_reaction(self):
        self.sampleReaction.save()
        url = reverse('reactions:reaction', kwargs={'reaction_id': 1})
        data = {
            'subject': 'subject-edit-test',
            'script': 'print("script-edit-test")',
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Reaction.objects.get().subject, 'subject-edit-test')

    def test_delete_reaction(self):
        self.sampleReaction.save()
        url = reverse('reactions:reaction', kwargs={'reaction_id': 1})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(models.Reaction.objects.all()), 0)
