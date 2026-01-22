import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SignalWatch.settings")

app = Celery("SignalWatch")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "gather_hourly_resources_task": {
        "task": "resources.tasks.gather_hourly_resources",
        "schedule": crontab(hour="*"),
    },
    "gather_daily_resources_task": {
        "task": "resources.tasks.gather_daily_resources",
        "schedule": crontab(day_of_week="*"),
    },
    "gather_weekly_resources_task": {
        "task": "resources.tasks.gather_weekly_resources",
        "schedule": crontab(day_of_week="*"),
    },
    "gather_monthly_resources_task": {
        "task": "resources.tasks.gather_monthly_resources",
        "schedule": crontab(day_of_week="1"),
    },
}
