from django.db import models
from main.models.user import User

from main.models.tag import Tag


class Task(models.Model):
    NEW_TASK = "new_task"
    IN_DEVELOPMENT = "in_development"
    IN_QA = "in_qa"
    IN_CODE_REVIEW = "in_code_review"
    READY_FOR_RELEASE = "ready_for_release"
    RELEASED = "released"
    ARCHIVED = "archived"
    TASK_STATES = [
        (NEW_TASK, "New Task"),
        (IN_DEVELOPMENT, "In Development"),
        (IN_QA, "In QA"),
        (IN_CODE_REVIEW, "In Code Review"),
        (READY_FOR_RELEASE, "Ready for Release"),
        (RELEASED, "Released"),
        (ARCHIVED, "Archived"),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField()
    state = models.CharField(max_length=255, choices=TASK_STATES, default=NEW_TASK)
    priority = models.PositiveIntegerField()
    author = models.ForeignKey(
        User, related_name="authored_tasks", on_delete=models.CASCADE
    )
    assigned = models.ForeignKey(
        User, related_name="assigned_tasks", on_delete=models.CASCADE
    )
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["priority"]
