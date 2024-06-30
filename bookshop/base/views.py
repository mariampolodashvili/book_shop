from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, User, Bestsellers, Series, Author, Genre
from django.db.models import Q


def home(request):
    search = request.GET.get("search") if request.GET.get('search') != None else ''
    if search:
        books = Book.objects.filter(Q(name__icontains=search) | Q(author__name__icontains=search))
        context = {"books": books}
        return render(request, 'base/books.html', context)
    else:
        bestseller_books = Bestsellers.objects.prefetch_related('books').all()
        context = {"bestseller_books": bestseller_books}
        return render(request, 'base/home.html', context)


def books(request):
    search = request.GET.get("search") if request.GET.get('search') != None else ''
    books = Book.objects.filter(Q(name__icontains=search) | Q(author__name__icontains=search) | Q(genre__name__icontains=search) )
    genres=Genre.objects.all()
    context = {"books": books, 'genres': genres}
    return render(request, 'base/books.html', context)

def series(request):
    search = request.GET.get("search") if request.GET.get('search') != None else ''
    if search:
        books = Book.objects.filter(Q(name__icontains=search) | Q(author__name__icontains=search))
        context = {"books": books}
        return render(request, 'base/books.html', context)
    else:
        series=Series.objects.all()
        context={"series" : series}
        return render(request, 'base/series.html', context)

def authors(request):
    search = request.GET.get("search") if request.GET.get('search') != None else ''
    if search:
        books = Book.objects.filter(Q(name__icontains=search) | Q(author__name__icontains=search))
        context = {"books": books}
        return render(request, 'base/books.html', context)
    else:
        authors=Author.objects.all()
        context = {"authors": authors}
        return render(request, 'base/authors.html', context)

def about(request):
    search = request.GET.get("search") if request.GET.get('search') != None else ''
    if search:
        books = Book.objects.filter(Q(name__icontains=search) | Q(author__name__icontains=search))
        context = {"books": books}
        return render(request, 'base/books.html', context)
    else:
        return render(request, 'base/about.html')

def profile(request, pk):
    search = request.GET.get("search") if request.GET.get('search') != None else ''
    if search:
        books = Book.objects.filter(Q(name__icontains=search) | Q(author__name__icontains=search))
        context = {"books": books}
        return render(request, 'base/books.html', context)
    else:
        user= User.objects.get(id=pk)
        books = user.books.all()
        context = {"books": books}
        return render(request, 'base/profile.html', context)