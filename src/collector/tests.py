from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ActionTest(APITestCase):

    def test_create_action(self):
        url = reverse('collector:collector')
        data = {
            'data': 'data-test',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
