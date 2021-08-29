# models.py
from django.db import models

class Memories(models.Model):
    date = models.DateField()
    text = models.TextField()
    def __str__(self):
        return str(self.date)