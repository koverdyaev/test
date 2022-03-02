import time

import requests
from celery.utils.log import get_task_logger
from django.conf import settings
from tenacity import retry, stop_after_attempt, wait_exponential

from config import celery_app

from .exceptions import TaskProcessingException
from .models import Task

CURSED_TIME = 13

logger = get_task_logger(__name__)


@celery_app.task()
def process_task(task_id: str):
    processing_time = get_task_processing_time(task_id)
    update_task_status(task_id=task_id, status=Task.Status.PROCESSING)
    try:
        preform_task(processing_time)
    except TaskProcessingException:
        logger.exception("Error during process_task.")
        update_task_status(task_id=task_id, status=Task.Status.ERROR)
        raise
    status = Task.Status.COMPLETED
    update_task_status(task_id=task_id, status=status)
    return status


def preform_task(processing_time: int):
    """Task stub."""
    time.sleep(processing_time)
    if processing_time == CURSED_TIME:
        raise TaskProcessingException("Something goes wrong.")


def update_task_status(task_id, status):
    base_url = get_base_url()
    url = f"{base_url}/tasks/{task_id}/"
    response = requests.patch(url, data={"status": status})
    logger.info(f"PATCH {url}; response status_code - {response.status_code}")


def get_base_url():
    host = settings.SERVICE_API_HOST
    port = settings.SERVICE_API_PORT
    return f"http://{host}:{port}"


@retry(stop=stop_after_attempt(3), wait=wait_exponential(min=0.2))
def get_task_processing_time(task_id: str):
    base_url = get_base_url()
    url = f"{base_url}/tasks/{task_id}/"
    response = requests.get(url)
    logger.info(f"PATCH {url}; response status_code - {response.status_code}")
    task_data = response.json()
    return task_data["processing_time"]
