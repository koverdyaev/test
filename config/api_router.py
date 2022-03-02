from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from server.tasks.api.views import TaskViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("tasks", TaskViewSet)


app_name = "api"
urlpatterns = router.urls
