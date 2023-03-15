from rest_framework import serializers
from main.models import user, tag, task


class UserSerializer(serializers.ModelSerializer):
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
