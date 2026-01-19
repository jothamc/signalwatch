from django.urls import path, include
from .views import ResourceModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ResourceModelViewSet, basename="resources")

urlpatterns = router.urls

# urlpatterns = [path("", ResourceModelViewSet.as_view({"get": "list"}))]
