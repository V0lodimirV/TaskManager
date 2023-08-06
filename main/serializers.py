from rest_framework import serializers
from main.models import user, tag, task
from django.core.files.base import File
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from task_manager import settings


class FileMaxSizeValidator:
    def __init__(self, max_size: int) -> None:
        self.max_size = max_size

    def __call__(self, value: File) -> None:
        if value.size > self.max_size:
            raise ValidationError(f"Maximum size {self.max_size} exceeded.")


class UserSerializer(serializers.ModelSerializer):
    avatar_picture = serializers.FileField(
        required=False,
        validators=[
            FileMaxSizeValidator(settings.UPLOAD_MAX_SIZES["avatar_picture"]),
            FileExtensionValidator(["jpeg", "jpg", "png"]),
        ]
    )
    class Meta:
        model = user.User
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = tag.Tag
        fields = ("title", "identifier")


class TaskSerializer(serializers.ModelSerializer):
    tag = TagSerializer(read_only=True, many=True)

    class Meta:
        model = task.Task
        fields = (
            "title",
            "description",
            "created_date",
            "modified_date",
            "due_date",
            "state",
            "priority",
            "author",
            "assigned",
            "tag",
        )
