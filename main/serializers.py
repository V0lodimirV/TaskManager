from rest_framework import serializers
from main.models import user, tag, task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user.User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "phone",
        )


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
            "tags",
        )
