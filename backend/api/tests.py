from django.contrib.auth.models import User
from django.test import TestCase


class SimpleTestCase(TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)

    def test_create_user(self):
        user = User.objects.create_user(
            username='test_user',
            password='test_123',
        )
        query = User.objects.filter(username='test_user')
        self.assertEqual(user, query.first())
