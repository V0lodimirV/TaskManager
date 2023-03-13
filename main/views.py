from main.models.user import User
from main.models.tag import Tag
from main.models.task import Task
from rest_framework import viewsets
from main.serializers import UserSerializer, TagSerializer, TaskSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by("id")
    serializer_class = UserSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.select_related("author", "assigned").prefetch_related(
        "tags"
    )
    serializer_class = TaskSerializer
