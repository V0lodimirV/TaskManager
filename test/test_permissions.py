from main.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from main.models import Task


class TaskDeleteViewTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword", is_staff=True
        )
        self.client.force_authenticate(user=self.user)
        self.task = Task.objects.create(title="Test task")

    def test_delete_task(self):
        response = self.client.delete(f"/api/tasks/{self.task.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_task_without_staff_permission(self):
        user = User.objects.create_user(
            username="testuser2", password="testpassword2", is_staff=False
        )
        self.client.force_authenticate(user=user)
        response = self.client.delete(f"/api/tasks/{self.task.id}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)