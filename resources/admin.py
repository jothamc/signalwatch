from django.contrib import admin
from .models import Resource, Snapshot

# Register your models here.

admin.site.register(Resource)
admin.site.register(Snapshot)