from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .serializers import ResourceSerializer
from .models import Resource

# Create your views here.


class ResourceModelViewSet(ModelViewSet):
    serializer_class = ResourceSerializer
    queryset = Resource.objects.all()
