# Generated by Django 4.1.6 on 2023-03-07 14:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_tag_task"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="due_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
