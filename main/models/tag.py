from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=255)
    identifier = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title
