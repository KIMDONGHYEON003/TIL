from django.db import models

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    rank = models.IntegerField()

    def __str__(self):
        return self.title