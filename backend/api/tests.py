"""Unit tests for API endpoints in the api app."""

from http import HTTPStatus

from api import models
from django.test import Client, TestCase


class TaskiAPITestCase(TestCase):
    """API tests for task listing and creation."""

    def setUp(self):
        """Set up a test client for API requests."""
        self.guest_client = Client()

    def test_list_exists(self):
        """Check that task list endpoint responds with 200."""
        response = self.guest_client.get('/api/tasks/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_task_creation(self):
        """Check that posting a task creates it and returns 201."""
        data = {'title': 'Test', 'description': 'Test'}
        response = self.guest_client.post('/api/tasks/', data=data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue(models.Task.objects.filter(title='Test').exists())
