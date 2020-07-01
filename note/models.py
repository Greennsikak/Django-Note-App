from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    topic = models.CharField(max_length=200, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model"""
        return self.topic

    class Meta:
        verbose_name_plural = 'Topic'


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='entry', null=True, blank=True)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text

    class Meta:
        verbose_name_plural = 'Entries'




