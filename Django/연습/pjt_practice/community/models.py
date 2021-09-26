from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = IntegerField()

    def __str__(self):
        return self.title