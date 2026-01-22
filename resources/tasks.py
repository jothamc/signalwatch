from celery import shared_task
from .models import Snapshot, Resource
from django.db.models import Q, Max
from .utils import fetch_snapshots, get_resources_query


@shared_task
def gather_hourly_resources():
    # Hourly resources
    print("Checking hourly now...")

    resources_to_process = get_resources_query(Resource.FREQ_HOURLY)

    fetch_snapshots(resources_to_process)


@shared_task
def gather_daily_resources():
    # Daily resources
    print("Checking daily now...")

    resources_to_process = get_resources_query(Resource.FREQ_DAILY)

    fetch_snapshots(resources_to_process)


@shared_task
def gather_weekly_resources():
    # Weekly resources
    print("Checking weekly now...")

    resources_to_process = get_resources_query(Resource.FREQ_WEEKLY)

    fetch_snapshots(resources_to_process)


@shared_task
def gather_monthly_resources():
    # Monthly resources
    print("Checking monthly now...")

    resources_to_process = get_resources_query(Resource.FREQ_MONTHLY)

    fetch_snapshots(resources_to_process)
