from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from ..models import Task
from ..tasks import process_task
from .serializers import (
    TaskCreateSerializer,
    TaskRetrieveSerializer,
    TaskUpdateSerializer,
)


class TaskViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    queryset = Task.objects.all()

    def perform_create(self, serializer) -> None:
        task = serializer.save()
        process_task.apply_async([task.task_id])

    def get_serializer_class(self):
        if self.action == "create":
            return TaskCreateSerializer
        if self.action in ("update", "partial_update"):
            return TaskUpdateSerializer
        return TaskRetrieveSerializer
