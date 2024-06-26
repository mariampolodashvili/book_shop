from django.db import models
from django.contrib.auth.models import AbstractUser



class Author(models.Model):
    name=models.CharField(max_length=200)
    birth = models.DateField(null=True)
    death = models.DateField(null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    picture = models.CharField(max_length=300)
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET("Unknown Author"))
    description = models.TextField(max_length=500)
    content = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.name} _ {self.author}"


class User(AbstractUser):
    books = models.ManyToManyField(Book, related_name='books', blank=True)



