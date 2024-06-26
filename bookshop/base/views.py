from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, User


def home(request):
    books = Book.objects.all()
    context={"books":books}
    return render(request, 'base/home.html', context)

def books(request):
    return render(request, 'base/books.html')

def series(request):
    return render(request, 'base/series.html')

def autors(request):
    return render(request, 'base/authors.html')

# def blog(request):
#     return render(request, 'base/blog.html')

def about(request):
    return render(request, 'base/about.html')

def profile(request, pk):
    user= User.objects.get(id=pk)
    books = user.books.all()
    context = {"books": books}
    return render(request, 'base/profile.html', context)