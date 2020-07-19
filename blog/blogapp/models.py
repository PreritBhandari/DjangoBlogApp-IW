from django.db import models

# Create your models here.
from django.utils import timezone


class Author(models.Model):
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.author


class Blog(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    post = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
