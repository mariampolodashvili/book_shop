from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, User, Bestsellers, Series, Author, Genre
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import MyUserCreationForm, BookForm


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

@login_required(login_url='login')
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

@login_required(login_url='login')
def adding(request, id):
    user=request.user
    book=Book.objects.get(id=id)
    user.books.add(book)
    return redirect('profile', request.user.id)


@login_required(login_url='login')
def delete(request, id):
    obj = Book.objects.get(id=id)
    if request.method=="POST":
        request.user.books.remove(obj)
        return redirect('profile', request.user.id)

    return render(request, 'base/delete.html', {'obj': obj} )

def login_user(request):
    if request.user.is_authenticated:
        return redirect('profile', request.user.id)
    if request.method == 'POST':
        username=request.POST.get('username').lower()
        password=request.POST.get('password')

        try:
            user=User.objects.get(username=username)
        except:
            pass

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile', request.user.id)
        else:
            pass
    return render(request, 'base/login.html')

def logout_user(request):
    logout(request)
    return redirect('home')


def registration(request):
    form=MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('profile', user.id)

        else:
            pass


    context = {'form': form}
    return render(request, 'base/registration.html', context)

def add_book(request):
    authors = Author.objects.all()
    genres =Genre.objects.all()
    form=BookForm()

    if request.method =='POST':
        book_author=request.POST.get('author')
        book_genre=request.POST.get('genre')

        author, created = Author.objects.get_or_create(name=book_author)
        genre, created = Genre.objects.get_or_create(name=book_genre)

        form = BookForm(request.POST)

        new_book = Book(picture=request.FILES['picture'], name=form.data['name'], author=author,
                        description=form.data['description'], price=form.data['price'])
        new_book.save()
        new_book.genre.add(genre)
        return redirect('books')


    context={'form': form, 'authors': authors, 'genres':genres}
    return render(request, 'base/add_book.html', context)