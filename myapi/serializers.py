# serializers.py

from rest_framework import serializers

from .models import Memories

class MemoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Memories
        fields = ('date', 'text')