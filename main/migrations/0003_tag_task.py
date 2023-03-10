# Generated by Django 4.1.6 on 2023-03-06 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_user_role"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("identifier", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("modified_date", models.DateTimeField(auto_now=True)),
                ("due_date", models.DateTimeField()),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("new_task", "New Task"),
                            ("in_development", "In Development"),
                            ("in_qa", "In QA"),
                            ("in_code_review", "In Code Review"),
                            ("ready_for_release", "Ready for Release"),
                            ("released", "Released"),
                            ("archived", "Archived"),
                        ],
                        default="new_task",
                        max_length=255,
                    ),
                ),
                ("priority", models.PositiveIntegerField()),
                (
                    "assigned",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assigned_tasks",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="authored_tasks",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("tags", models.ManyToManyField(to="main.tag")),
            ],
            options={
                "ordering": ["priority"],
            },
        ),
    ]
