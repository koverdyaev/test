import uuid

from django.db import models


class Task(models.Model):
    class Status(models.IntegerChoices):
        NEW = 1
        PROCESSING = 2
        COMPLETED = 3
        ERROR = 4

    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    processing_time = models.IntegerField()
    status = models.SmallIntegerField(choices=Status.choices, default=Status.NEW)
