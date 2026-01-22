from requests import get
import hashlib

from django.db.models import Max, Q
from django.utils import timezone

from .models import Resource, Snapshot


def get_resources_query(freq):
    timedelta = None
    if freq == Resource.FREQ_HOURLY:
        timedelta = timezone.now() - timezone.timedelta(hours=1)
    elif freq == Resource.FREQ_DAILY:
        timedelta = timezone.now() - timezone.timedelta(days=1)
    elif freq == Resource.FREQ_WEEKLY:
        timedelta = timezone.now() - timezone.timedelta(days=7)
    elif freq == Resource.FREQ_MONTHLY:
        timedelta = timezone.now() - timezone.timedelta(days=30)
    else:
      raise Exception("Frequency not recognized")

    return (
        Resource.objects.annotate(latest_snapshot_date=Max("snapshot__capture_date"))
        .filter(
            # 2. Now filter based on that specific date
            Q(latest_snapshot_date__isnull=True)
            | Q(latest_snapshot_date__lte=timedelta),
            is_snapshotting=True,
            monitoring_frequency=freq,
        )
        .values("id", "url", "type")
    )


def fetch_snapshots(objs: list[dict[str, str]]):
    print("OBJS:", objs)
    for obj in objs:

        url = obj["url"]
        try:
            response = get(url=url)
            content = (
                response.json()
                if obj["type"] == Resource.TYPE_JSON
                else (response.content)
            )

            Snapshot.objects.create(
                resource_id=obj["id"],
                content_hash=hashlib.sha256(content).hexdigest(),
                status_code=response.status_code,
                size=(len(response.content)),
            )

        except Exception as e:
            print(e)
