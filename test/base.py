from rest_framework.test import APIClient, APITestCase
from main.models import User
from django.urls import reverse
from typing import Union, List
from http import HTTPStatus


class TestViewSetBase(APITestCase):
    user: User = None
    client: APIClient = None
    basename: str

    @classmethod
    def setUpTestData(cls) -> None:
        super().setUpTestData()
        cls.user = cls.create_api_user()
        cls.client = APIClient()

    @staticmethod
    def create_api_user(user_attributes):
        return User.objects.create(**user_attributes)

    @classmethod
    def detail_url(cls, key: Union[int, str]) -> str:
        return reverse(f"{cls.basename}-detail", args=[key])

    @classmethod
    def list_url(cls, args: List[Union[str, int]] = None) -> str:
        return reverse(f"{cls.basename}-list", args=args)

    def create(self, data: dict, args: List[Union[str, int]] = None) -> dict:
        self.client.force_login(self.user)
        response = self.client.post(self.list_url(args), data=data)
        assert response.status_code == HTTPStatus.CREATED, response.content
        return response.data
