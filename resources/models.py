from django.db import models
from django.utils import timezone

# Create your models here.


class Resource(models.Model):
    TYPE_HTML = "HTML"
    TYPE_JSON = "JSON"
    TYPE_TEXT = "TEXT"

    RESOURCE_TYPES = {
        TYPE_HTML: "HTML",
        TYPE_JSON: "JSON",
        TYPE_TEXT: "TEXT",
    }
    FREQ_HOURLY = "HOUR"
    FREQ_DAILY = "DAY"
    FREQ_WEEKLY = "WEEK"
    FREQ_MONTHLY = "MONT"

    FREQUENCIES = {
        FREQ_HOURLY: "Hourly",
        FREQ_DAILY: "Daily",
        FREQ_WEEKLY: "Weekly",
        FREQ_MONTHLY: "Monthly",
    }

    url = models.URLField()
    type = models.CharField(choices=RESOURCE_TYPES, max_length=4, default=TYPE_HTML)
    monitoring_frequency = models.CharField(
        choices=FREQUENCIES, max_length=4, default=FREQ_DAILY
    )
    is_active = models.BooleanField(default=True)
    is_snapshotting = models.BooleanField(default=False)
    registration_date = models.DateTimeField(default=timezone.now)
    
    

class Snapshot(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    capture_date = models.DateTimeField(default=timezone.now) 
    content_hash = models.TextField()
    status_code = models.IntegerField()
    size = models.IntegerField()

