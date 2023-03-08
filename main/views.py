from main.models.user import User
from main.models.tag import Tag
from main.models.task import Task
from rest_framework import viewsets
from main.serializers import UserSerializer, TagSerializer, TaskSerializer
import django_filters


class UserFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = User
        fields = ("name",)


class TaskFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    description = django_filters.CharFilter(lookup_expr="icontains")
    author = django_filters.ModelChoiceFilter(queryset=User.objects.all())
    assigned = django_filters.ModelChoiceFilter(queryset=User.objects.all())
    tags = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all())

    class Meta:
        model = Task
        fields = ["state", "priority", "due_date"]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by("id")
    serializer_class = UserSerializer
    filterset_class = UserFilter


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.select_related("author", "assigned").prefetch_related(
        "tags"
    )
    serializer_class = TaskSerializer
