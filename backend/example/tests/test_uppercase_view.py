from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APIClient


class UppercaseViewTests(TestCase):
    url = reverse_lazy('uppercase_text')

    def setUp(self):
        self.client = APIClient()

    def test_uppercase_empty_string(self):
        response = self.client.get(self.url + '?text=')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'text': ''})

    def test_uppercase_string(self):
        response = self.client.get(self.url + '?text=test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'text': 'TEST'})

    def test_uppercase_string_already_uppercase(self):
        response = self.client.get(self.url + '?text=TEST')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'text': 'TEST'})
