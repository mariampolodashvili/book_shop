from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, User, Bestsellers, Series, Author, Genre, Comment
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import MyUserCreationForm, BookForm, UserForm
from .seeder import seeder_dunc
from django.contrib import messages

def home(request):
    search = request.GET.get("search") if request.GET.get('search') != None else ''
    seeder_dunc()
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
    books = list(dict.fromkeys(books))
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
    total_price=0
    if search:
        books = Book.objects.filter(Q(name__icontains=search) | Q(author__name__icontains=search))
        context = {"books": books}
        return render(request, 'base/books.html', context)
    else:
        user= User.objects.get(id=pk)
        books = user.books.all()
        for book in books:
            total_price+=book.price
        context = {"books": books, 'total_price': total_price}
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

@login_required(login_url='login')
def drop(request, id):
    book =Book.objects.get(id=id)
    if request.method=='POST':
        book.picture.delete()
        book.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'book': book })

def login_user(request):
    if request.user.is_authenticated:
        return redirect('profile', request.user.id)
    if request.method == 'POST':
        username=request.POST.get('username').lower()
        password=request.POST.get('password')

        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist!')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile', request.user.id)
        else:
            messages.error(request, 'User or Password is not exist!')
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
            messages.error(request, 'Follow the instructions and create proper user and password')


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
                        description=form.data['description'], price=form.data['price'], creator=request.user )

        if not (Book.objects.filter(picture=request.FILES['picture'])):
            new_book.save()
            new_book.genre.add(genre)
        else:
            messages.error(request, 'Book with same picture already existx...')

        return redirect('books')


    context={'form': form, 'authors': authors, 'genres':genres}
    return render(request, 'base/add_book.html', context)


def book(request, id):
    book = Book.objects.get(id=id)
    book_comments=book.comment_set.all() #.order_by('-created')
    author=Author.objects.get(name=book.author)
    if request.method == "POST":
        Comment.objects.create(
            user = request.user,
            book=book,
            body=request.POST.get('body')
        )
    return  render(request, 'base/book.html', {'book': book, 'author': author, 'comments': book_comments})

def author(request, id):
    author = Author.objects.get(id=id)
    return render(request, 'base/author.html', {'author': author})

def serie(request, id):
    serie=Series.objects.get(id=id)
    context={'serie':serie, 'author': author}
    return render(request, 'base/serie.html', context)

@login_required(login_url='login')
def update_user(request):
    user=request.user
    form=UserForm(instance=user)

    if request.method == 'POST':
        form=UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', user.id)


    context = {'form': form}
    return render(request, 'base/update_user.html', context)


def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    book=comment.book
    if request.method=='POST':
        comment.delete()
        return redirect('book', book.id)
    return render(request, 'base/delete.html', {'obj' : comment} )