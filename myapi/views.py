# views.py
from rest_framework import viewsets

from .serializers import MemoriesSerializer
from .models import Memories


class MemoriesViewSet(viewsets.ModelViewSet):
    queryset = Memories.objects.all()
    serializer_class = MemoriesSerializer