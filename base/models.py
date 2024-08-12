from django.db import models
from django.contrib.auth.models import AbstractUser



class Author(models.Model):
    picture = models.CharField(max_length=300)
    name=models.CharField(max_length=200)
    birth = models.DateField(null=True)
    death = models.DateField(null=True)
    country=models.CharField(null=True,max_length=200 )
    description=models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Price(models.Model):
    price=models.FloatField(max_length=100)

    def __str__(self):
        return str(self.price)

class Categories(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Age(models.Model):
    age_range=models.CharField(max_length=100)

    def __str__(self):
        return self.age_range


class Book(models.Model):
    creator= models.ForeignKey('User', on_delete=models.SET("Unknown Creator"))
    picture = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    genre=models.ManyToManyField(Genre, related_name="books", blank=True)
    categories=models.ForeignKey(Categories, related_name="books", blank=True, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(Author, on_delete=models.SET("Unknown Author"))
    price = models.ForeignKey(Price, related_name="books", blank=True, null=True, on_delete=models.SET_NULL)
    age_range=models.ForeignKey(Age, related_name="books", blank=True, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} _ {self.author}"


class User(AbstractUser):
    books = models.ManyToManyField(Book, related_name='books', blank=True)
    avatar = models.ImageField(null=True, default='avatar.jpg')
    bio = models.TextField(null=True)


class Bestsellers(models.Model):
    books=models.ManyToManyField(Book, related_name='bestseller_books', blank=True)


class Series(models.Model):
    title=models.CharField(max_length=200)
    picture = models.CharField(max_length=300)
    book = models.ManyToManyField(Book, related_name='book', blank=True)

class Comment(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.body





