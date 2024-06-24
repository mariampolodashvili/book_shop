from django.db import models
from django.contrib.auth.models import AbstractUser


class Book(models.Model):
    picture = models.CharField(max_length=300)
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    content = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} _ {self.author}"


